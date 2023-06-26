import pandas as pd

dados = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
# print(dados)

dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]"]]

dados_pt = dados[dados["Country Name"] == "Portugal"]


print(dados_pt)
