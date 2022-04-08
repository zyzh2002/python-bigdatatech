s=[9,7,8,3,2,1,5,6]
for i in range(0,len(s)):
    if s[i] %2 == 0:
        j = s[i]
        s[i] = pow(j,2)
outputString = ""
for i in s:
    outputString += (str(i) + ",")

print(outputString[:-1])