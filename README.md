[<img alt="Pyppeteer" src="https://img.shields.io/badge/Pyppeteer-175510?style=flat&logo=Puppeteer&logoColor=white"/> <img alt="Python" src="https://img.shields.io/badge/Python-11db00?style=flat&logo=python&logoColor=white"/>](https://pyppeteer.github.io/pyppeteer/) <img alt="PySimpleGUI" src="https://img.shields.io/badge/PySimpleGUI-008000?style=flat&logo=python&logoColor=white"/> ![GitHub](https://img.shields.io/github/license/Agille-Cred/botWhatsApp) ![GitHub repo size](https://img.shields.io/github/repo-size/Agille-Cred/botWhatsApp) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Agille-Cred/botWhatsApp)

![Executável do botWhatsApp v1.4](assets/app.png)

## Instruções

Para executar:
- Escreva a mensagem, e insira uma planilha com duas colunas (sem cabeçalhos) de Nomes e Números (com 19, sem traços ou espaços).
- Precisará entrar no WhatsApp Web com o celular, escaneando o QRCode quando solicitado.
- Após o bot executar o script, será gerado uma planilha com Nomes e Números de mensagens não enviadas.

### Bibliotecas

**Utilizando [Python Pandas](https://pandas.pydata.org/), [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/), [pyppeteer](https://github.com/pyppeteer/pyppeteer) e [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/).**
```
pip install pandas pyppeteer pysimplegui openpyxl
```

### Executável

Para criar um executável (.exe), use o [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe) ou com o [pyinstaller](https://github.com/pyinstaller/pyinstaller), o comando:
```
pyinstaller --noconfirm --onefile --windowed --icon "icone.ico" --name "NomeDoExecutavel"  "botWhatsapp.py"
```

**Qualquer alteração no projeto é bem-vinda.**
