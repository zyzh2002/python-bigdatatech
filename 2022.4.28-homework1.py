import csv
csvF = []
with open("./stu-scores.csv","r") as csvFile:
    csvReader =csv.reader(csvFile)
    for row in csvReader:
        csvF.append(row)
print("所有学生信息")
for i in csvF:
    print(i)

print("学号和平均值")
for i in csvF[1:]:
    print("%s,%.2f"%(i[0],(int(i[1])+int(i[2])+int(i[3]))/3))
