import pandas as pd
import os

os.system("cls")

# Caixa de Menu
print(" ======================================================")
print("|                                                      |")
print("|     Ferramenta de Cálculo de Variação Percentual     |")
print("|                          de                          |")
print("|            Consumo de Energia Eléctrica              |")
print("|                                                      |")
print(" ======================================================")

# Função para cálculo da variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_inicial - consumo_final) / consumo_inicial * 100

dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")

dados_portugal = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")

dados_portugal = dados_portugal[["Country Name", "1990 [YR1990]","2000 [YR2000]"]]
dados_pt = dados_portugal[dados_portugal["Country Name"] == "Portugal"]
consumo_ano_inicial = dados_pt['1990 [YR1990]'].values[0]
consumo_ano_final = dados_pt['2000 [YR2000]'].values[0]

variacao_percentual = calcular_variacao_percentual(consumo_ano_inicial, consumo_ano_final)
print()

print(
    f"A variação percentual no consumo de energia eléctrica em Portugal entre 1990 e 2000 foi de: {variacao_percentual:.2f}%")

print()


#(estudar forma de carregar os cabeçalhos do ficheiro)
dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]","2013 [YR2013]","2014 [YR2014]","2015 [YR2015]","2016 [YR2016]","2017 [YR2017]","2018 [YR2018]","2019 [YR2019]","2020 [YR2020]","2021 [YR2021]","2022 [YR2022]",]]

lista_anos_i=["2013","2014","2015","2016","2017","2018","2019","2020","2021"]

lista_anos_f=["2014","2015","2016","2017","2018","2019","2020","2021","2022"]

#Escolher o País onde se pretende consultar a variação
escolhe_pais = input("Em que outro país deseja consultar a variação? ")
print()

continuar_i = False
continuar_f = False

dados_pais = dados[dados["Country Name"] == escolhe_pais]

# Escolher ano inicial
ano_i = input("Introduza o ano inicial entre 2013 e 2021: ")
print()
while continuar_i == False:
    
    if ano_i in lista_anos_i:
        if dados_pais[ano_i + " [YR" + ano_i + "]"].values[0] != "..":
            continuar_i = True
        else:
            ano_i = input("O ano que colocou não contém dados para este País, introduza outro ano inicial entre 2013 e 2021: ")
            print()
            continuar_i = False    
    else:
        continuar_i = False
        ano_i = input("O ano que colocou é inválido, introduza o ano inicial entre 2013 e 2021: ")
        print()


# Escolher ano final
ano_f = input("Introduza o ano final entre 2014 e 2022: ")
print()
while continuar_f == False:
    
    if ano_f in lista_anos_f:
        if dados_pais[ano_f + " [YR" + ano_f + "]"].values[0] != "..":
            continuar_f = True
        else:
            ano_f = input("O ano que colocou não contém dados para este País, introduza outro ano inicial entre 2013 e 2021: ")
            print()
            continuar_i = False      
    else:
        continuar_f = False
        ano_f = input("O ano que colocou é inválido, introduza o ano final entre 2014 e 2022: ")
        print()

dados_ano_inicio = dados_pais[ano_i + " [YR" + ano_i + "]"].values[0]
dados_ano_fim = dados_pais[ano_f + " [YR" + ano_f + "]"].values[0]

variacao_percentual_pais = calcular_variacao_percentual(dados_ano_inicio, dados_ano_fim)

print(
    f"A variação percentual no consumo de energia eléctrica em {escolhe_pais} entre {ano_i} e {ano_f} foi de: {variacao_percentual_pais:.2f}%")

print()









