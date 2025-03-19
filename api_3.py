import requests
import json

import urllib.request
url = 'https://data.gov.lv/dati/dataset/40d80be5-0c09-47c4-80f3-fad4bec19f33/resource/c32c7afd-0d05-44fd-8b24-1de85b4bf11d/download/meteo_stacijas.csv'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())