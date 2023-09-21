import csv

prog = list()

with open("Benigndata.csv", 'r') as fileIn:
    readIn = csv.reader(fileIn)
    
    with open("Benigndata2.csv", 'w', newline='') as fileOut:
        writeOut = csv.writer(fileOut)
        
        for idx, row in enumerate(readIn):
            if row == []:
                prog.append(idx)
            else:
                writeOut.writerow(row)

with open("data_for_Benigndata.txt", 'w') as Data:
    Data.write("Number of files removed: %s\n" % len(prog))
    one = [1]*len(prog)
    real = [x+y for x, y in zip(prog, one)]
    Data.write("The removed files are: %s" % real)

