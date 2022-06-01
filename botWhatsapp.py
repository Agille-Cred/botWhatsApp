import asyncio, time
import pandas as pds
import PySimpleGUI as sg
from pyppeteer import launch
from functions.planilha import import_planilha
from functions.output import output

icone = 'assets\icon.ico'
font = ("Arial 12 bold")
sg.theme()

layout = [
    [
        sg.Text("Mensagem      ", font=font, justification='center')
    ],
    [
        sg.Text("Olá [nome], ", font="Arial 8 bold", justification='left')  
    ],
    [
        sg.Multiline(size=(65,3), key='-texto-')
    ],
    [
        sg.Text("Planilha de Contatos", font=font), sg.In(
            size=(30, 1), enable_events=True, key='-planilha-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Green',  key='-planilha-', 
                                  file_types=(("XLSX files", "*.xlsx"),))
    ],
    [
        sg.Button('Mandar Mensagens', size=(39, 1), font="Arial 15 bold")
    ]
]

window = sg.Window('Bot WhatsApp', layout, icon=icone)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Mandar Mensagens':

        texto = values['-texto-']
        local_planilha = values['-planilha-']

        if texto == '':
            sg.popup("Insira uma mensagem", font=font)
            continue
        
        if local_planilha == '':
            sg.popup("Insira um arquivo de planilha", font=font)
            continue
             
        if texto != '' and local_planilha != '':
            
            try:
              planilha = import_planilha(local_planilha)
            except:
              sg.popup("Erro ao importar planilha", font=font)
            
            # Pyppeteer
            try:
                          
                async def mandarMensagem(texto, planilha):

                    df_numeros_invalidos = pds.DataFrame()
                    browser = await launch(headless=False)
                    page = await browser.newPage()
                    await page.goto('https://web.whatsapp.com/')
                    time.sleep(20)

                    for contato in range(int(len(planilha))):
                        nome = planilha.iloc[contato][0]
                        mensagem = "Olá {}. {}".format(nome, texto)
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

                            df_numeros_invalidos.loc[tam + 1, 'Nome'] = nome
                            df_numeros_invalidos.loc[tam + 1, 'Contato'] = numero
                            continue
                        
                        try:
                            await page.click("span[data-testid='send']")
                        except:
                            df_numeros_invalidos.loc[tam + 1, 'Nome'] = nome
                            df_numeros_invalidos.loc[tam + 1, 'Contato'] = numero
                            continue
                        else:
                            print('Mensagem enviada a {} no número {}'.format(nome, numero))
                        
                        
                        time.sleep(2)

                    await browser.close()
                    output(df_numeros_invalidos)
                    sg.popup("Mensagens enviadas", font=font)

                asyncio.run(mandarMensagem(texto, planilha))
            except Exception as e:
                sg.popup("{}\nErro ao mandar mensagens. Tentar novamente.".format(e), font=font)


window.close()
