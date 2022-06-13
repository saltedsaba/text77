#運動會獎牌與獎牌數(字典) #已完成
a = int(input("輸入比數:"))
dict1 = {} #dict 字典
for i in range(a):
        b,c = input("輸入獎牌:").split()
        dict1[b] = c
for j in dict1: #j=key
        print(f'{j}牌得到{dict1[j]}面')



