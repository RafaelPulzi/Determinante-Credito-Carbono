import pandas
import requests


response = requests.get("https://api.coinbase.com/v2/prices/MCO2-BRL/spot")
data = response.json()
preco = float(data["data"]["amount"])

tabela = pandas.read_csv("dados.csv", sep =",")
tabela


tabela['C02Evitado'] = (0.013840*(tabela['dap']**2.437632))*(tabela['altura']*0.428609) #Biomassa presa nos fustes em t ha
tabela['C02Evitado'] = tabela['C02Evitado']*0.5 #EC
tabela['C02Evitado'] = tabela['C02Evitado']*3.67 #Conversao para Co2 em t ha
print(tabela['C02Evitado'].sum())
creditosDeCarbono = (tabela['C02Evitado'].sum()/1000).tolist()

print(creditosDeCarbono*preco)
