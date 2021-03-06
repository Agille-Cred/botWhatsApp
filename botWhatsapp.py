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
        sg.Text("Mensagem", font=font, justification='center')
    ],
    [
        sg.Text("Olá [nome]. ", font="Arial 8 bold", justification='left')  
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
        sg.Button('Mandar Mensagens', size=(39, 1), font="Arial 15 bold", key='botaoEnviar')
    ],
    [
        sg.ProgressBar(100, orientation='h', s=(43,12), key='progbar', bar_color="Green")
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
            window['botaoEnviar'].update(disabled=True)
            window['progbar'].update(bar_color="Red")
            try:
              planilha = import_planilha(local_planilha)
            except:
              sg.popup("Erro ao importar planilha", font=font)
            
            # Pyppeteer
            try:
                          
                async def mandarMensagem(texto, planilha):

                    numeros_n_enviados = pds.DataFrame()
                    browser = await launch(headless=False)
                    page = await browser.newPage()
                    await page.goto('https://web.whatsapp.com/', options={"waitUntil": "domcontentloaded"})
                    
                    envios = 0
                    TentativaAtual = 0
                    NumerodeTentativas = 5

                    while(True):
                        try:
                            await page.waitForSelector('#app > div > div > div.ldL67._3sh5K > div > div > div.WM0_u > span')
                            break
                        except print(0):
                            if(++TentativaAtual == NumerodeTentativas):
                                print('Esperando o QRCODE ser validado, tentativa atual: ', TentativaAtual)
                            else:
                                pass
                    
                    mensagens = int(len(planilha))
                    
                    for contato in planilha.iloc:
                        nome = contato[0]
                        numero = contato[1]
                        mensagem = "Olá {}. {}".format(nome, texto)
                        link = 'https://web.whatsapp.com/send?phone=55{}&text={}'.format(
                            numero, mensagem)
                        tam = int(len(numeros_n_enviados))
                        await page.goto(link, options={"waitUntil": "domcontentloaded"})
                        await page.waitForSelector("._3Lm9O")
                        time.sleep(2)
                        
                        try:
                            await page.waitForSelector(".g0rxnol2")
                            await page.click("span[data-testid='send']")
                            await page.waitFor(3000)
                        except:
                            numeros_n_enviados.loc[tam + 1, 'Nome'] = nome
                            numeros_n_enviados.loc[tam + 1, 'Contato'] = numero
                            print('Mensagem não enviada a {} no número: {}'.format(nome, numero))
                            continue
                        else:
                            print('Mensagem enviada a {} no número: {}'.format(nome, numero))
                            envios += 1
                            window['progbar'].UpdateBar(envios,mensagens)
                        
                        time.sleep(3)

                    await browser.close()
                    output(numeros_n_enviados)
                    window['botaoEnviar'].update(disabled=False)
                    sg.popup("{} Mensagens enviadas.\n{} Não enviadas.".format(mensagens - tam, tam), font=font)

                asyncio.run(mandarMensagem(texto, planilha))
            except Exception as e:
                sg.popup("{}\nErro ao mandar mensagens. Tentar novamente.".format(e), font=font)


window.close()
