# Dota Latvijas atvērto datu vietne – data.gov.lv. Jums tiek piedāvāta 2018. gada datu kopa
# „Atkritumu šķirošanas punkti”. Izveidot pieprasījumu uz doto resursu un apstrādāt tā atbildi,
# izvadot tikai tos atkritumu šķirošanas punktus, kuros var nodot kādu no šiem atkritumu veidiem:
# baterijas un akumulatorus vai nolietotās riepas, vai metālu. Izvadīt konkrētā punkta adresi
# un novada nosaukumu. Nodrošināt, ka programma analizē ārējā resursa atbildi, ja ārējais
# resurss neatbild, tad programmai jāizvada atbilstošs paziņojums. Ja ārējais resurss atbild ar
# tukšu atbildi, arī veikt atbilstoša teksta izvadi.
# Pieprasījuma adrese uz šo resursu pieejama šeit:
# https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444eaaca-ae90c120cc3d
# Datu kolonnu atšifrējumi:
# „0 : Papīrs” – ir nododams papīrs.
# „1 : Plastmasa” – ir nododama plastmasa.
# „2 : Stikls” – ir nododams stikls.
# „3 : Metāls” – ir nododams metāls.
# „4 : Bioloģiski noārdāmie atkritumi” – ir nododami bioloģiski noārdāmie atkritumi.
# „5 : Tekstilmateriāli” – ir nododami tekstilmateriāli.
# „6 : Elektriskās un elektroniskās iekārtas” – ir nododamas elektriskās un elektroniskās iekārtas.
# „7 : Apgaismes iekārtas un spuldzes” – ir nododamas apgaismes iekārtas un spuldzes.
# „8 : Baterijas un akumulatori” – ir nododamas baterijas un akumulatori.
# „9 : Sadzīvē radušies bīstamie atkritumi” – ir nododami sadzīvē radušies bīstamie atkritumi.
# „10 : Nolietotās riepas” – ir nododamas nolietotās riepas.
# Burts „x” norāda, ka konkrētajā punktā ir iespējas nodot attiecīgos atkritumus.
# 1.1. Izveidot izsaukumu uz doto resursu (2 punkti).
# 1.2. Analizēt ārējā resursa atbildi, vai tas atbild ar korektu atbildi (2 punkti).
# 1.3. Izvadīt atbilstošu tekstu, ja serveris neatbild (2 punkti).
# 1.4. Izvadīt atbilstošu tekstu, ja serveris atbild ar tukšu (tukšu masīvu) atbildi (1 punkts).
# 1.5. Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot baterijas un
# akumulatorus (1 punkts).
# 1.6. Izvadīt attiecīgā atkritumu nodošanas punkta novada nosaukumu, kurā var nodot baterijas
# un akumulatorus (1 punkts).
# 1.7. Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot nolietotās riepas
# (1 punkts).
# 1.8. Izvadīt attiecīgā atkritumu nodošanas punkta novada nosaukumu, kurā var nodot nolietotās
# riepas (1 punkts).
# 1.9. Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot metālu (1 punkts).
# 1.10. Izvadīt attiecīgā atkritumu nodošanas punkta novada nosaukumu, kurā var nodot metālu
# (1 punkts).

import requests

# API URL
url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search"
params = {
    "resource_id": "92ac6e57-c5a5-444e-aaca-ae90c120cc3d"
}

try:
    # Veic pieprasījumu uz API
    response = requests.get(url, params=params)
    
    # Pārbauda servera atbildi
    if response.status_code != 200:
        print("Serveris neatbild. Lūdzu, mēģiniet vēlreiz vēlāk.")
    else:
        data = response.json()
        
        # Pārbauda, vai atbilde nav tukša
        if not data.get("result", {}).get("records", []):
            print("Atbilde ir tukša.")
        else:
            records = data["result"]["records"]
            print("Šķirošanas punkti, kur pieņem noteiktus atkritumu veidus:\n")

            for record in records:
                address = record.get("Adrese")
                municipality = record.get("Municipality")
                
                # Pārbauda, vai pieņem atbilstošus atkritumus
                if "x" in record.get("8 : Baterijas un akumulatori", "").lower():
                    print(f"Baterijas un akumulatori: {address}, {municipality}")
                if "x" in record.get("10 : Nolietotās riepas", "").lower():
                    print(f"Nolietotās riepas: {address}, {municipality}")
                if "x" in record.get("3 : Metāls", "").lower():
                    print(f"Metāls: {address}, {municipality}")

except requests.exceptions.RequestException as e:
    print("Radās kļūda, savienojoties ar API:", e)

