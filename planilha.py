import pandas as pds
import sys

def import_planilha():
    try:
        file = ('contatos.xlsx')
        data = pds.read_excel(file, names=["Nome","Contato"])

        # Código de PROPOSTA/VR CMS para tipo str
        # data1['PROPOSTA'] = data1['PROPOSTA'].astype(str)
        
        data['Nome'] = data['Nome'] .astype(str)
        data['Contato'] = data['Contato'].astype(str)

        print(data)
    except:
        print("IMPORT PLANILHA Não Efetuado")
        sys.exit(0)
    else:
        print("IMPORT PLANILHA OK")

    return data

import_planilha()