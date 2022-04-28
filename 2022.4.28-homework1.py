import csv
csvF = []
with open("./read-csv-avg.vsv") as csvFile:
    csvReader =csv.reader(csvFile)
    for row in csvReader:
        csvF.append(row)
    csvFile.close()
