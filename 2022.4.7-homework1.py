a = 2
b = 1
sum = 0
for i in range(0,20):
    sum += a/b
    c = b
    b = a
    a +=c

print("%.2f"%sum)