# https://www.squash.io/processing-csv-files-in-python/
import csv

# with open('agenti.csv', mode ='r')as file:
#   csvFile = csv.reader(file)
#   for lines in csvFile:
#         print(lines)


with open('agenti.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)


with open("agenti.csv", "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        pilseta = int(row[3])
        if pilseta == "Rīga":
            print(row)