import requests
import json

url = "https://github.com/SkolotajsZelukins/macibu_api/blob/main/query.json"
response = requests.get(url)
data = response.json()  # Assuming the response is in JSON format
print(data)