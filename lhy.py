primeList = []
for i in range(100,1000):
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag == True:
         primeList.append(i)

outStr = ""
for i in range(0,len(primeList)):
    outStr += str(primeList[i])
    if (i+1) % 5 == 0:
        outStr += "\n"
    else:
        outStr += " "

print(outStr)