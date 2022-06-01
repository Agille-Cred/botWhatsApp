# botWhatsApp

[![GitHub license](https://img.shields.io/github/license/renatocfrancisco/botWhatsapp)](https://github.com/renatocfrancisco/botWhatsapp)![GitHub repo size](https://img.shields.io/github/repo-size/renatocfrancisco/botWhatsapp)

**Utilizando [Python Pandas](https://pandas.pydata.org/), [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/), [pyppeteer](https://github.com/pyppeteer/pyppeteer) e [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/).**

Para executar: **`.xlsx`** com nomes e contatos.
Precisará entrar no WhatsApp Web com o QRCode quando solicitado.
```
pip install pandas pyppeteer pysimplegui openpyxl
```

Para criar um executável (.exe), use o [**auto-py-to-exe**](https://github.com/brentvollebregt/auto-py-to-exe) ou com o [**pyinstaller**](https://github.com/pyinstaller/pyinstaller), o comando:
```
pyinstaller --noconfirm --onefile --windowed --icon "icone.ico" --name "NomeDoExecutavel"  "botWhatsapp.py"
```

Qualquer alteração no projeto é bem-vinda.