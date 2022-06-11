x = [13, 5, 17, 12, 9, 2, 8]

for index in range(1, len(x)):
    elementToSort = x[index]
    preIndex = index - 1
    while x[preIndex] > elementToSort and preIndex >= 0:
        x[preIndex+1] = x[preIndex]
        preIndex -= 1
    x[preIndex+1] = elementToSort

print(x)