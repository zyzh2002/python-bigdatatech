import math

n = 5
triangle = [[math.comb(row, column) for column in range(0, n)]
            for row in range(0, n)]
print(triangle)

#for row in range(0,n):
#    for column in range(0,n):
#        triangle[row][column] = math.comb(row,column)
#print(triangle)
