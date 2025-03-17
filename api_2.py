import requests
import json
url = requests.get("https://github.com/SkolotajsZelukins/macibu_api/blob/main/saraksts.json") 
info = requests.get(url).json()
print(info)
print(info['result']['records'])
