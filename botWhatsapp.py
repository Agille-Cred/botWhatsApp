import asyncio
from pyppeteer import launch
import PySimpleGUI as sg
from planilha import import_planilha
from texto import import_texto
from output_df import output
import time
import pandas as pds

icone = 'assets\icon.ico'
font = ("Arial 12 bold")
sg.theme()

layout = [
    [
        sg.Text("Arquivo de Texto       ", font=font), sg.In(
            size=(30, 1), enable_events=True, key='-texto-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Black',  key='texto',
                                  file_types=(("TXT files", "*.txt"),))
    ],
    [
        sg.Text("Planilha de Contatos", font=font), sg.In(
            size=(30, 1), enable_events=True, key='-planilha-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Green',  key='planilha',
                                  file_types=(("XLSX files", "*.xlsx"),))
    ],
    [
        sg.Button('Mandar Mensagens', size=(39, 1), font="Arial 15 bold", )
    ]
]

window = sg.Window('Bot WhatsApp', layout,
                   element_justification='center', icon=icone)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Mandar Mensagens':

        local_texto = values['-texto-']
        local_planilha = values['-planilha-']
        
        # Teste
        local_texto = 'texto.txt'
        local_planilha = 'teste.xlsx'
        
        if local_texto != '' and local_planilha != '':
        
            texto = import_texto(local_texto)
            planilha = import_planilha(local_planilha)

            async def main(texto, planilha):

                df_numeros_invalidos = pds.DataFrame()
                browser = await launch(headless=False)
                page = await browser.newPage()
                await page.goto('https://web.whatsapp.com/')
                time.sleep(20)

                for contato in range(int(len(planilha))):
                    nome = planilha.iloc[contato][0]
                    mensagem = 'Bom dia, {}! Como está?\n \n {}'.format(nome, texto)
                    numero = planilha.iloc[contato][1]
                    link = 'https://web.whatsapp.com/send?phone=55{}&text={}'.format(
                        numero, mensagem)
                    await page.goto(link)
                    time.sleep(10)
                    
                    try:
                        inp = await page.waitFor('._3J6wB')
                    except:
                        print('Numero {} é válido.'.format(numero))
                    else:
                        print('numero {} é inválido.'.format(numero))
                        tam = int(len(df_numeros_invalidos)) 
                        
                        df_numeros_invalidos.loc[tam + 1,'Nome'] = nome
                        df_numeros_invalidos.loc[tam + 1,'Contato'] = numero
                        continue
                        
                    time.sleep(5)
                    await page.click("span[data-testid='send']")
                    time.sleep(3)
                    print('Mensagem enviada a {} no número {}'.format(nome, numero))

                await browser.close()
                output(df_numeros_invalidos)
               
            asyncio.get_event_loop().run_until_complete(main(texto, planilha))

window.close()
