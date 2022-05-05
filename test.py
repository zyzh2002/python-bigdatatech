import csv


a = open("./stu-scores.csv")
b = []
c = csv.reader(a)

for i in range(2):
    print(next(c))
    a.seek(0)