def f(n):
    if n == 1 or n == 2 or n == 3:  # 数列前三项的值都为1
        return 1
    else:
        return f(n-1) + f(n-2) + f(n-3)  # 从第4项开始某项是前三项之和


for i in range(1, 20):
    print(str(f(i))+",", end="")  # 输出前19项的值
print(f(20), end="")  # 输出第20项的值
