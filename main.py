import csv
import os

path = '/Users/parikhoberoi/Downloads/Extract Data/Extract Data/'
results = []
source = []
for file in [f for f in os.listdir(path) if '.csv' in f]:
    source.append(file)
results.append([])
for File in source:
    with open(path + File) as f:
        reader = csv.reader(f)
        next(reader)
        answer = max(reader, key=lambda column: float(column[6].replace(',', '')))
        results.append(answer)

file = open('/Users/parikhoberoi/Desktop/Results.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(results)