# !PySG.New - Template Snippet
# !PySG.Text - Text Snippet
# !PySG.Button -Button Snippet
# !PySG.Input -Input Snippet
# !PySG.Spin -Spin Snippet
# !PySG.Theme -Theme Snippet

import PySimpleGUI as sg
from planilha import import_planilha
from texto import import_texto

icone = 'assets\icon.ico'
font = ("Arial 12 bold")
sg.theme()

layout = [
    [
        sg.Text("Arquivo de Texto       ",font=font), sg.In(
            size=(30, 1), enable_events=True, key='-texto-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Black',  key='texto',
                                  file_types=(("TXT files", "*.txt"),))
    ],
    [
        sg.Text("Planilha de Contatos",font=font), sg.In(
            size=(30, 1), enable_events=True, key='-planilha-'),
        sg.FileBrowse(button_text="Procurar", font=font, button_color='Green',  key='planilha',
                                  file_types=(("XLSX files", "*.xlsx"),))
    ],
    [
        sg.Button('Mandar Mensagens', size=(30,1), font="Arial 15 bold", )
    ]
]

window = sg.Window('Bot WhatsApp', layout, element_justification='center', icon=icone)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Mandar Mensagens':
        
        local_texto = values['-texto-']
        texto = import_texto(local_texto)
        
        local_planilha = values['-planilha-']
        planilha = import_planilha(local_planilha)
        

window.close()
