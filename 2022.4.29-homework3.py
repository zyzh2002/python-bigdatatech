#读取csv文件输出至少有一门课不及格的学生所有信息
import csv
with open("stu-scores.csv", "r") as f:
    r = csv.reader(f)  # 通过csv.reader()对象读出文件所有的信息
    print("所有学生信息（含表头）")
    for i in r:  # 按行输出r中所有信息
        print(i)
    f.seek(0)  #文件指针移至文件开始的位置
    next(f) #跳过表头
    print("\n至少有一门课不及格学生信息")
    for i in r:  # 遍历r中每行信息
        x = min(int(i[1]), int(i[2]), int(i[3]))  # 找到每个学生最小的一个成绩
        if x < 60:  # 判断最小成绩x是否小于60
            print(i)  # 输出至少有一门课不及格的学生所有信息
