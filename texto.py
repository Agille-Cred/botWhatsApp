import sys

def import_texto(local):
    try:
      file = open(local,'r', encoding="utf8")
      texto = file.read()
      print(texto)
    except:
      sys.exit(0)
      
    return texto