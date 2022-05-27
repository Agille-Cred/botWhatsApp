import asyncio
from pyppeteer import launch
from planilha import import_planilha
from texto import import_texto

async def main():
    
    import_texto()
    
    planilha = import_planilha()
    
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://web.whatsapp.com/')
    await page.screenshot({'path': 'example.png'})
    await browser.close()
    
    for contato in range(int(len(planilha))):
        nome = planilha.iloc[contato][0]
        mensagem = 'Bom dia, {}! Como esta?\n \nSou o *, analista de RH da *. O motivo do meu contato é referente ao seu interesse pela vaga de Agente de Negócios.\n \nComo primeira etapa do processo seletivo, há uma Avaliação de Conhecimentos Gerais e Tecnologias, que deverá ser realizada Online.\n \nSegue o link da avaliação: https://forms.gle/okysgNL59BAgxxyi6\n \nA avaliação de conhecimentos ficará disponível até segunda-feira, 30/05/2022 às 09h00.\n \nSe ficou alguma dúvida, entre em contato comigo por aqui mesmo.\n \nEspero te encontrar em breve!'.format(nome)
        numero = planilha.iloc[contato][1]
        link = 'https://api.whatsapp.com/send?phone=55{}&text={}'.format(numero, mensagem)
        print(link)
         
    # await page.goto('https://web.whatsapp.com/send?phone=+'+phone[0]+'&text='+mensagem+'');

asyncio.get_event_loop().run_until_complete(main())