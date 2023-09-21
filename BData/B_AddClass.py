import csv

Class = "0"

with open("Benigndata2.csv", 'r') as fileIn:
    readIn = csv.reader(fileIn)
    
    with open("Benigndata3.csv", 'w', newline = '') as fileOut:
        writeOut = csv.writer(fileOut)
        
        for row in readIn:
            row.append(Class)
            writeOut.writerow(row)