#学号和成绩按成绩排序后分别输出到文件中和屏幕上
s=[["2125",90],["2113",88],["2104",63],["2129",95]] #学生学号和成绩
t=sorted(s,key=lambda x:x[1],reverse=True)  #按成绩降序排序
print("sno score")  #字符串"sno score"输出到屏幕上
for i,j in t:  #数据输出到屏幕上
    print(i,j)

f=open("d:\\cj.txt","w") #在c:\下创建数据文件cj.txt
f.write("sno score\n")  #字符串"sno score\n"输出到cj.txt文件中
for i,j in t:
    f.write("%s %s"%(i,j)+"\n")  #每个学生学号和成绩输出到文件中
f.close()  #关闭文件

