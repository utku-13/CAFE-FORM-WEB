import csv

with open(file='cafe-dat.csv', mode='a') as cf:
    csv_writer = csv.writer(cf)
    csv_writer.writerow(['Name', 'Age', 'City'])