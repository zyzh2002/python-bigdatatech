def getElement(list, i, j):
    row = list[i-1]
    value = row[j-1]
    return value


p = int(input())
matrix = []
for i in range(0, p):
    row = []
    for j in range(0, p):
        row.append(int(input()))
    matrix.append(row)

sum = 0
for i in range(1, p+1):
    sum += getElement(matrix, i, i)

for i in range(1, p+1):
    sum += getElement(matrix, i, p+1-i)
if p % 2 != 0:
    sum -= getElement(matrix, int((p+1)/2), int((p+1)/2))

print(matrix)
print(sum)
