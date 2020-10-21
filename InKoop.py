import csv

with open('C:\Users\jithin\Downloads\hotels.csv','r') as file:
    reader = csv.reader(file)

    for read in reader:
        print(read)















