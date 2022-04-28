import csv
with open("./read-csv-avg.vsv") as csvFile:
    csvReader =csv.reader(csvFile)
    for row in csvReader:
        print(row)
