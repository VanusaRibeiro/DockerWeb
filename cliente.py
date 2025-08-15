import requests

response = requests.get("http://api:5000/api")
print("Resposta da API:", response.json())
