# 字典diicTXL和dicOther分别存储小明的通讯录和舍友通讯录信息，通信录中包括姓名、手机号和QQ号信息
dicTXL = {'小新': ['13913000001', '18181220001'],
          '小亮': ['13913000002', '18191220002'],
          '小刚': ['13913000003', '18191220003']}
dicOther = {'大刘': ['13914000001', '18191230001'],
            '大王': ['13914000002', '18191230002'],
            '大张': ['13914000003', '18191230003']}
# 将字典dicOther合并到字典dicTXL中
dicTXL.update(dicOther)
# dicWX字典存储同学的微信号
dicWX = {'小新': 'xx9907',
         '小刚': 'gang1004',
         '大王': 'jack_w',
         '大刘': 'liu666'}
# 将微信号添加至字典dicTXL中
for dicTXL_k, dicTXL_v in dicTXL.items():
    if dicTXL_k in dicWX:
        dicTXL[dicTXL_k].append(dicWX[dicTXL_k])
    else:
        dicTXL_v.append(dicTXL_v[0])
      # 更新字典dicTXL中键值对
    pass
lt = dicTXL['大王']
lt[0] = '13914000004'

xm = input()
for i in dicTXL[xm]:
    print(i)
