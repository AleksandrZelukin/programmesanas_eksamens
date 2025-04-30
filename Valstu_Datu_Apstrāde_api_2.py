# Uzdevuma apraksts
# Pēc dotās saites https://restcountries.com/v3.1/all ir pieejams API, 
# kas sniedz dažāda veida datus par valstīm visā pasaulē. 
# Izmantojot šo API, izveido programmu, kurā izpildīti visi dotie uzdevumi!

# Uzdevumi
# Izveido pieprasījumu uz doto API. (1 punkts)
# Pārbaudi, vai no servera ir saņemta korekta atbilde. (1 punkts)
# Iegūsti un izvadi visu valstu vispārpieņemtos nosaukumus (“name” → “common”). (2 punkti)
# Iegūsti un izvadi kopējo valstu skaitu. (2 punkti)
# Iegūsti un izvadi visu valstu vidējo iedzīvotāju skaitu (“population”). (2 punkti)
# Iegūsti un izvadi valsti ar vislielāko iedzīvotāju skaitu. (2 punkti)
# Iegūsti un izvadi visu valstu kopējo platību (“area”). (2 punkti)
# Iegūsti un izvadi informāciju par Latvijas:
# apakšreģionu (“subregion”); (2 punkti)
# robežvalstu kodiem (“borders”). (2 punkti)

import requests
import json
pieprasijums = requests.get("https://restcountries.com/v3.1/all") # Izveido pieprasījumu uz doto API
if pieprasijums.status_code == 200: # Pārbaudi, vai no servera ir saņemta korekta atbilde
    dati = pieprasijums.json()


valstu_vards = [country.get('name', {}).get('common', 'Unknown') for country in dati]
print("Visu valstu vispārpieņemtos nosaukumus:")
for vards in valstu_vards:
    print(vards) # Iegūsti un izvadi visu valstu vispārpieņemtos nosaukumus (“name” → “common”). (2 punkti)
        

total_countries = len(dati)
print(f"kopējo valstu skaits: {total_countries}") # Iegūsti un izvadi kopējo valstu skaitu. (2 punkti)
    

populations = [country.get('population', 0) for country in dati if 'population' in country]

average_population = sum(populations) / len(populations)
print(f"visu valstu vidējo iedzīvotāju skaits: {average_population:.2f}") 
# Iegūsti un izvadi visu valstu vidējo iedzīvotāju skaitu (“population”). (2 punkti)


max_population_country = max(dati, key=lambda x: x.get('population', 0))
print(f"valsts ar vislielāko iedzīvotāju skaitu: {max_population_country.get('name', {}).get('common', 'Unknown')}")
# Iegūsti un izvadi valsti ar vislielāko iedzīvotāju skaitu. (2 punkti)
print(f"iedzīvotāju skaits: {max_population_country.get('population', 0)}")
      
total_area = sum(country.get('area', 0) for country in dati if 'area' in country)
print(f"visu valstu kopējo platība: {total_area} km²")
# Iegūsti un izvadi visu valstu kopējo platību (“area”). (2 punkti)

latvia_info = next((country for country in dati if country.get('name', {}).get('common', '') == 'Latvia'), None)

subregion = latvia_info.get('subregion', 'Unknown')
borders = latvia_info.get('borders', [])
print(f"informāciju par Latvijas apakšreģionu: {subregion}") # Iegūsti un izvadi informāciju par Latvijas apakšreģionu (“subregion”); (2 punkti)
print(f"Latvijas robežvalstu kodi: {borders}") # robežvalstu kodiem (“borders”). (2 punkti)