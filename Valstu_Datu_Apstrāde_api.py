# Uzdevuma apraksts
# Pēc dotās saites https://restcountries.com/v3.1/all ir pieejams API, 
# kas sniedz dažāda veida datus par valstīm visā pasaulē. Izmantojot šo API, 
# izveido programmu, kurā izpildīti visi dotie uzdevumi!
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

# Import necessary libraries
import requests
import json
import pandas as pd
# Fetch data from the API
response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code == 200:
    countries_data = response.json()
else:
    print("Failed to fetch data from the API")
    countries_data = []

# # Convert data to a pandas DataFrame
if countries_data:
    df = pd.json_normalize(countries_data)

    # Save the DataFrame to a CSV file
    df.to_csv("countries_data.csv", index=False, encoding='utf-8')
    print("Data saved to countries_data.csv")
else:
    print("No data to process")
    
# Extract and print all common names of countries
if countries_data:
    common_names = [country.get('name', {}).get('common', 'Unknown') for country in countries_data]
    print("Common names of countries:")
    for name in common_names:
        print(name)
            
# Get and print the total number of countries
if countries_data:
    total_countries = len(countries_data)
    print(f"Total number of countries: {total_countries}")
    
    
# Calculate and print the average population of all countries
if countries_data:
    populations = [country.get('population', 0) for country in countries_data if 'population' in country]
    if populations:
        average_population = sum(populations) / len(populations)
        print(f"Average population of all countries: {average_population:.2f}")
    else:
        print("No population data available to calculate the average.")
        
# Find and print the country with the largest population
if countries_data:
    most_populous_country = max(countries_data, key=lambda country: country.get('population', 0))
    country_name = most_populous_country.get('name', {}).get('common', 'Unknown')
    population = most_populous_country.get('population', 0)
    print(f"The country with the largest population is {country_name} with a population of {population}.")
    
# Calculate and print the total area of all countries
if countries_data:
    total_area = sum(country.get('area', 0) for country in countries_data if 'area' in country)
    print(f"Total area of all countries: {total_area:.2f} square kilometers.")
    
# Extract and print information about Latvia
latvia_info = next((country for country in countries_data if country.get('name', {}).get('common') == 'Latvia'), None)
if latvia_info:
    subregion = latvia_info.get('subregion', 'Unknown')
    borders = latvia_info.get('borders', [])
    print(f"Latvia's subregion: {subregion}")
    print(f"Latvia's border country codes: {', '.join(borders) if borders else 'None'}")
else:
    print("Latvia's information is not available.")