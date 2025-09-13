import csv
# Writing to a CSV file using csv.writer
# Writing to a CSV file using csv.DictWriter


data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

with open('api_5.csv', mode='a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)


data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}
]

with open('api_5.csv', mode='a', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)