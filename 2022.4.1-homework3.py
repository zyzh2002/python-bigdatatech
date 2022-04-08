dic_score = {'012': [90, 94, 85, 54, 68, 75, 71, 21],
             '005': [8, 75, 21, 65, 89, 97, 25, 75],
             '108': [87, 54, 78, 25, 14, 98, 67, 57],
             '037': [45, 87, 54, 82, 95, 91, 57, 32],
             '066': [95, 67, 51, 48, 98, 92, 80, 39],
             '020': [85, 81, 65, 97, 35, 62, 71, 84]}
dic_avg = {}  # 存放平均分
for k, v in dic_score.items():
    v_min = min(v)  # 求最低分
    v_max = max(v)  # 求最高分
    v_sum = sum(v)  # 求总分
    v_sum = v_sum-v_max-v_min  # 从总分中去除最大值和最小值
    v_avg = v_sum/(len(v)-2)  # 求平均分
    dic_avg[k] = v_avg  # 将参赛者编号和平均值存入字典dic_avg中
# 按照平均分由大到小排序
lt_avg = [(v, k) for k, v in dic_avg.items()]
lt_avg.sort(reverse=True, key=(lambda a: a[0]))  # 由大到小排序
lt_avg = [(v, k) for k, v in lt_avg]
dic_avg = {v: k for v, k in lt_avg}  # 将列表lt_avg转换为字典dic_avg
# 输出结果
for k, v in dic_avg.items():
    print(k, v)
