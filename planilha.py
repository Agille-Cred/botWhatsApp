import pandas as pds

def import_planilha(local):
    try:
        file = local
        data = pds.read_excel(file, names=["Nome","Contato"], header=None)
        
        data['Nome'] = data['Nome'] .astype(str)
        data['Contato'] = data['Contato'].astype(str)

        print(data)
    except:
        print("IMPORT PLANILHA Não Efetuado")
    else:
        print("Planilha OK")

    return data