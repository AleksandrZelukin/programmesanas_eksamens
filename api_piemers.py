import requests

# city = 'Riga'

# url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
# weather_info = requests.get(url).json()

# temperature = weather_info['main']['temp']

# print(temperature)

# Izveidot API pieprasījumu norādītajai tīmekļa vietnei un atbilstoši uzdevuma  nosacījumiem apstrādāt iegūtos datus.

# Dota Latvijas atvērto datu vietne – data.gov.lv. Jums tiek piedāvāta 2018. gada datu kopa „Atkritumu šķirošanas punkti”. 
# Izveidot pieprasījumu uz doto resursu un apstrādāt tā atbildi, izvadot tikai tos atkritumu šķirošanas punktus, 
# kuros var nodot kādu no šiem atkritumu veidiem:  baterijas un akumulatorus vai nolietotās riepas, vai metālu. 
# Izvadīt konkrētā punkta  adresi un novada nosaukumu. Nodrošināt, ka programma analizē ārējā resursa atbildi, 
# ja ārējais resurss neatbild, tad programmai jāizvada atbilstošs paziņojums. 
# Ja ārējais resurss atbild ar tukšu atbildi, arī veikt atbilstoša teksta izvadi.

# url2 = 'https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444eaaca-ae90c120cc3d'
# atkritumu_punkti = requests.get(url2).json()
# print(atkritumu_punkti)
# info = atkritumu_punkti['help']['records']
# print(info)


import urllib.request
url = 'https://data.gov.lv/dati/api/3/action/datastore_search?resource_id=17460efb-ae99-4d1d-8144-1068f184b05f&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())

import urllib.request
url = 'https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
# print(fileobj.read())
atkritumu_punkti = requests.get(url).json()
print(atkritumu_punkti)