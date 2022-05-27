def import_texto(local):
    try:
      file = open(local,'r', encoding="utf8")
      texto = file.read()
      print(texto)
    except:
      print("Erro ao importar texto")
    else:
      print("Texto OK")
      
    return texto