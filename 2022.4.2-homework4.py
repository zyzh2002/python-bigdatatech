# 小麦原始数据
data = {"20180041": [231, 80.6, 578.1],
        "20180040": [233, 78.6, 571.3],
        "20180069": [253, 82.5, 571.2],
        "20180036": [230, 85.9, 581.5],
        "20180048": [228, 79.2, 560.2]}
# 插入序号初值均设为1
for i in data:
    data[i].append(1)
# 提取变量data中所有键对应的值
lst = []
for i in data.values():
    lst.append(i)
# 按亩产量由高到低添加序号
for i in range(4):
    for j in range(i+1, 5):
        if lst[i][2] > lst[j][2]:  # 亩产量值小序号加1
            lst[j][3] = lst[j][3]+1
        else:
            lst[i][3] = lst[i][3]+1
# 替换变量data中所有键值对
t = 0
for i in data:
    data[i] = lst[t]  # 替换变量data中所有键值对
    t = t + 1
    print(i, data[i])  # 输出变量data的值
