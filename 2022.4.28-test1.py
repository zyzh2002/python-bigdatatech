lst = [0,1,2]
res = []
def perm(start: int, end: int):
    global lst
    if start == end:
        res.append(lst.copy())
    else:
        for i in range(start, end+1):
            lst[start], lst[i] = lst[i], lst[start]
            perm(start+1, end)
            lst[start], lst[i] = lst[i], lst[start]
perm(0, 2)

dicts = []

dicts.append({0:1,1:2,2:3})
dicts.append({0:1,1:2,2:4})
dicts.append({0:1,1:3,2:4})
dicts.append({0:2,1:3,2:4})

ans = []
for i in res:
    for j in dicts:
        ans.append([j[k] for k in i])

print("共有%d个,分别是"%len(ans))
for i in ans:
    ostr = ""
    for j in i:
        ostr += str(j+1)
    print(ostr)