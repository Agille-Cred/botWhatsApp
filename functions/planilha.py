import pandas as pds

def import_planilha(local):
    
    file = local
    data = pds.read_excel(file, header=None)
    
    data[0] = data[0].astype(str)
    data[1] = data[1].astype(str)
    
    return data