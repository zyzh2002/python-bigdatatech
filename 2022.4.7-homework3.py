#杨辉三角数据矩阵
n=int(input())    #矩阵行数
lst=[[1],[1,1]]    #前两行数据放到列表变量lst中
if n==1:print(lst[0][0])    #只输出第一行数据
elif n==2:    #只输出前两行数据
    for i in range(n):    
        for j in range(i+1):
            print(lst[i][j],end=" ")
        print()
else:    #计算三行或三行以上数据
    for i in range(2,n):
        t=[1]   #第i+1行第一个数据是1
        for j in range(1,i):
            x= lst[i-1][j-1]+lst[i-1][j]  #计算每行中间数据
            t.append(x)    #追加行数据
        t.append(1)    #第i+1行最后一个数据是1
        lst.append(t)    #将第i+1行添加到列表变量lst中
    #输出n行数据矩阵（n在[3,10]之间）
    for i in range(n):    
        for j in range(i+1):
            print(lst[i][j],end=" ")    #输出每行数据
        print()    #输出一行数据后换行
     

