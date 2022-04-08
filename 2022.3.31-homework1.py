from numpy import outer


def printInFormat(lst: list, inf: str) -> None:
    print(inf)
    for i in lst:
        print(str(i[0])+" "+str(i[1]))


def printInFormat_modified(lst: list, inf: str) -> None:
    print(inf)
    out_str = ""
    for i in lst:
        out_str += (str(i[0])+" "+str(i[1])+"\n")
    print(out_str[:-1], end="")


lst1 = [("028", 90), ("017", 75), ("002", 40), ("005", 65),
        ("002", 40), ("033", 78), ("017", 75), ("027", 32)]


def getSortKey(lst): return int(lst[0])


lst1.sort(key=getSortKey)
printInFormat(lst1, "去重前学号和成绩")

s = set({})
s.update(lst1)
lst2 = []
for i in s:
    lst2.append(i)

lst2.sort(key=getSortKey)
printInFormat(lst2, "去重后学号和成绩")

lst3 = []
for i in lst2:
    if int(i[1]) < 60:
        lst3.append(i)

lst3.sort(key=getSortKey)
printInFormat_modified(lst3, "不及格学生学号和成绩")
