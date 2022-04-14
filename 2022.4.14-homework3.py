def f1(d):
    t=[]  #存放每门成绩均>=85的学生学号
    for k,v in d.items():
        if min(v)>=85:t.append(k)   #满足条件的学号添加到列表变量t中
    return t

def f2(d):
    t=[]  #存放每个学生总分和平均分
    for k,v in d.items():
         t.append((v[0]+v[1]+v[2],round((v[0]+v[1]+v[2])/3,2)))  #列表变量t中添加总分和平均分，其中平均分保留两位小数
    return t

def f3(d):
    dd=sorted(d.items(),key=lambda x:sum(x[1]))  #按总分升序排序形成列表对象dd
    t=[]
    for i in dd:
        t.append(i[0])  #列表变量t中添加按总分升序排序的学号
    return t


d={'01':[67,88,45],'02':[97,68,85],'03':[97,98,95],'04':[67,48,45],'05':[82,58,75],'06':[96,49,65]}
print("每门成绩均>=85的学生学号：",f1(d))
print("每个学生总分和平均分：",f2(d))
print("按总分升序排列的学号列表：",f3(d))

