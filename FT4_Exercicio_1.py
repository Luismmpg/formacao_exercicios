import pandas as pd

# Função para cálculo da variação percentual


def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_inicial-consumo_final) / consumo_inicial * 100


dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
# print(dados)

dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]"]]
dados_pt = dados[dados["Country Name"] == "Portugal"]
consumo_ano_1990 = dados_pt["1990 [YR1990]"].values[0]
consumo_ano_2000 = dados_pt["2000 [YR2000]"].values[0]

variacao_percentual_pt = calcular_variacao_percentual(
    consumo_ano_1990, consumo_ano_2000)

print(variacao_percentual_pt)

# print(dados_pt)
