from pandas import ExcelWriter

def output(df_output):

    writer1 = ExcelWriter('planilha_numerosInvalidos.xlsx')

    df_output.to_excel(writer1, index=False)
    print("OUTPUT OK\n")

    writer1.save()