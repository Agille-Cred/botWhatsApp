from pandas import ExcelWriter

def output(df_output):

    try:
        writer1 = ExcelWriter('planilha_numerosInvalidos.xlsx')
        df_output.to_excel(writer1, index=False)
        writer1.save()
    except:
        print('Erro ao gerar planilha de números inválidos')
    else:
        print("Output OK")
