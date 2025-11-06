import requests
import json

# import urllib.request
# url = 'https://data.gov.lv/dati/dataset/40d80be5-0c09-47c4-80f3-fad4bec19f33/resource/c32c7afd-0d05-44fd-8b24-1de85b4bf11d/download/meteo_stacijas.csv'  
# fileobj = urllib.request.urlopen(url)
# print(fileobj.read())


# import urllib.request
# url = 'https://data.gov.lv/dati/dataset/8f9d7452-3c64-4a0c-bb50-489fa0335f22/resource/277165b4-1a1c-4ebf-a7f4-364f36347128/download/venta_aizsargjoslu-kategorijas_gala.csv'  
# fileobj = urllib.request.urlopen(url)

# for line in fileobj:
#     if line.decode('utf-8').strip() == "Baltijas jūra no Papes ezera kanāla līdz Sventājai":
#         print(line.decode('utf-8').strip())


url = 'https://data.gov.lv/dati/dataset/8f9d7452-3c64-4a0c-bb50-489fa0335f22/resource/277165b4-1a1c-4ebf-a7f4-364f36347128/download/venta_aizsargjoslu-kategorijas_gala.csv'  
info = requests.get(url).text.splitlines()

for line in info:
    if line.strip() == "476; 376364; Oksle; L;  ; 12094; 3; 0;  ; 3; Venta; 3,76364E+11":
        print(line.strip())
