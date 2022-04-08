inList = eval(input())
x = int(input())
indexList = []
for i in range(0,len(inList)-1):
    if inList[i] == x:
        indexList.append(i)


if len(indexList) == 0:
    print("not found")
else:
    print(str(x)+"出现在"+str(inList)+"中的位置")
    for i in indexList:
        print("第%d位置"%(i+1))