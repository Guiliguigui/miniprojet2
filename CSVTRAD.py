import csv

with open('auto.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        print(row)

  