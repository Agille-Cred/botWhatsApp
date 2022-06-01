def import_texto(local):

    file = open(local,'r', encoding="utf8")
    texto = file.read()
    print(texto)

    print("Texto OK")
      
    return texto