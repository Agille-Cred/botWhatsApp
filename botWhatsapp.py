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
        mensagem = 'Olá, {}'.format(nome)
        numero = planilha.iloc[contato][1]
        link = 'https://api.whatsapp.com/send?phone=55{}&text={}'.format(numero, mensagem)
        print(link)
         
    # await page.goto('https://web.whatsapp.com/send?phone=+'+phone[0]+'&text='+mensagem+'');

asyncio.get_event_loop().run_until_complete(main())