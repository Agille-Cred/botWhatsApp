import pandas as pds
import sys

def import_planilha(local):
    try:
        file = local
        data = pds.read_excel(file, names=["Nome","Contato"])
        
        data['Nome'] = data['Nome'] .astype(str)
        data['Contato'] = data['Contato'].astype(str)

        print(data)
    except:
        print("IMPORT PLANILHA Não Efetuado")
        sys.exit(0)
    else:
        print("IMPORT PLANILHA OK")

    return data