import requests

response = requests.get("https://api.coinbase.com/v2/prices/MCO2-BRL/spot")
data = response.json()
preco = data["data"]["amount"]
