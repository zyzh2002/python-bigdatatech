def f(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum==n

for i in range(1,1000):
    if f(i) == True:
        print(i)