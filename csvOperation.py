csvData = []
with open("stu-scores.csv", "r") as csvFile:
    for i in csvFile:
        i = i[:-1]
        csvData.append(i.split(","))

print(csvData)

with open("stu-scores.csv", "a") as writeObject:
    for i in csvData:
        writeStr = ""
        for j in i:
            writeStr = writeStr + j + ","
        writeStr = writeStr[:-1]
        writeStr += "\n"
        writeObject.write(writeStr)
