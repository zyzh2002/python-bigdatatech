import random
lst = ['A', 'B', 'C', 'D', 'E']  # 定义一个含有五个元素的列表，用来存放这五个同学的名次顺序
while True:
    random.shuffle(lst)
    if (lst.index('D') == 1 or lst.index('B') == 2) and (lst.index('C') == 1 or lst.index('E') == 3) and (lst.index('E') == 0 or lst.index('A') == 4) and (lst.index('C') == 2 or lst.index('A') == 3) and (lst.index('B') == 1 or lst.index('D') == 4):
        print(lst)
        break
