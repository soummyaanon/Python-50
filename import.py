import csv

data = []
with open('/Users/soumyaram/Downloads/python1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        data.append(row)

print(data)