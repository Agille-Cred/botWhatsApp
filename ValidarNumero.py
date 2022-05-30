import asyncio
from pyppeteer import launch
import PySimpleGUI as sg
from planilha import import_planilha
from output_df import output
from texto import import_texto
import time
import pandas as pds

icone = 'assets\icon.ico'
font = ("Arial 12 bold")
sg.theme()

layout = [
    [
        sg.Text("Planilha de Contatos", font=font), sg.In(
            size=(30, 1), enable_events=True, key='-planilha-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Green',  key='planilha',
                                  file_types=(("XLSX files", "*.xlsx"),))
    ],
    [
        sg.Button('Validar numeros', size=(30, 1), font="Arial 15 bold", )
    ]
]

window = sg.Window('Validador Whatsapp', layout,
                   element_justification='center', icon=icone)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Validar numeros':

        local_planilha = values['-planilha-']
        
        if local_planilha != '':

            planilha = import_planilha(local_planilha)

            async def main(planilha):
                
                df_numeros_invalidos = pds.DataFrame()
                browser = await launch(headless=False)
                page = await browser.newPage()
                await page.goto('https://web.whatsapp.com/')
                time.sleep(10)

                for contato in range(int(len(planilha))):
                    nome = planilha.iloc[contato][0]
                    numero = planilha.iloc[contato][1]
                    link = 'https://web.whatsapp.com/send?phone=55{}'.format(numero)
                    await page.goto(link)
                    time.sleep(11)
                    
                    try:
                        inp = await page.waitFor('._3J6wB')
                        print('Número {} é inválido.'.format(numero))
                        tam = int(len(df_numeros_invalidos))  
                        
                        df_numeros_invalidos.loc[tam + 1,'Nome'] = nome
                        df_numeros_invalidos.loc[tam + 1,'Contato'] = numero
                    except:
                        print('Número {} é válido.'.format(numero))
                        
                    
                await browser.close()
                
                output(df_numeros_invalidos)
               
            asyncio.get_event_loop().run_until_complete(main(planilha))

window.close()
