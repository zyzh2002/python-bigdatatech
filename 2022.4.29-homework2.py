def isprime(x):
    try:
        for i in range(2,x):  # i是判断x是否为质数的除数
            if x % i == 0:
                return False  # 不是质数
        else:
            return True  # 是质数
    except:  # 不是整数（包括实数，字符串等）
        return -1


n = [23, 12, "abc", 34.6]
for i in n:
    if isprime(i) == -1:  # 不是整数
        print("{}不是整数".format(i))
    elif isprime(i) ==True:  # 是质数
        print("{}是质数".format(i))
    elif isprime(i) ==False:  # 不是质数
        print("{}不是质数".format(i))
