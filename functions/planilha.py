import pandas as pds

def import_planilha(local):
    
    file = local
    data = pds.read_excel(file, names=["Nome","Contato"], header=None)
    
    data['Nome'] = data['Nome'] .astype(str)
    data['Contato'] = data['Contato'].astype(str)

    print(data)
    
    print("Planilha OK")

    return data