import csv 

def read_csv(dataFile):
    with open(dataFile, 'r') as file:
        csvreader = csv.reader(file)
    return csvreader