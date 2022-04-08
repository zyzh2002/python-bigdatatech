length = int(input())
lst = []
for i in range(0, length):
    lst.append(int(input()))

s_lst = lst.copy()
s_lst.sort()

if s_lst == lst:
    print("True")
else:
    print("False")
