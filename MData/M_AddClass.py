import csv

Class = "1"

with open("Maldata2.csv", 'r') as fileIn:
    readIn = csv.reader(fileIn)
    
    with open("Maldata3.csv", 'w', newline = '') as fileOut:
        writeOut = csv.writer(fileOut)
        
        for row in readIn:
            row.append(Class)
            writeOut.writerow(row)