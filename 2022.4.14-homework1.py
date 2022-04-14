def getAvg(lst: list) -> float:
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)


s = {'小李': [77, 54], '小张': [89, 66, 78, 99], '小陈': [90], '小杨': [69, 58, 93]}

newS = {}

for i, j in s.items():
    newS[i] = int(getAvg(j))

print(newS)
