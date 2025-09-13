# https://www.squash.io/processing-csv-files-in-python/
import csv

with open("agenti.csv", "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    pilseta = input("Ievadi pilsētu: ") # e.g., Rīga
    print(f"Agenti pilsētā {pilseta}:")
    for row in csv_reader:
        if row[2] == pilseta:
            print(row)
        
        # if pilseta in row[2]:
        #     print(row)