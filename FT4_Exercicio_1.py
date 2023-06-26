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
    return (consumo_inicial-consumo_final) / consumo_inicial * 100

dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
dados2 = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
# print(dados)

#estudar forma de carregar os cabeçalhos do ficheiro
dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]","2013 [YR2013]","2014 [YR2014]","2015 [YR2015]","2016 [YR2016]","2017 [YR2017]","2018 [YR2018]","2019 [YR2019]","2020 [YR2020]","2021 [YR2021]","2022 [YR2022]",]]

#Escolher o País onde se pretende consultar a variação
escolhe_pais = input("Em que país deseja consultar a variação? ")

dados_pt = dados[dados["Country Name"] == escolhe_pais]
consumo_ano_1990 = dados_pt["1990 [YR1990]"].values[0]
consumo_ano_2000 = dados_pt["2000 [YR2000]"].values[0]
variacao_percentual_pt = calcular_variacao_percentual(consumo_ano_1990, consumo_ano_2000)
print()

print(
    f"A variação percentual no consumo de energia eléctrica em {escolhe_pais} entre 1990 e 2000 foi de: {variacao_percentual_pt:.2f}%")

print()










