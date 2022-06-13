#運動會獎牌與獎牌數(串列) #已完成

a=int(input("輸入比數n:"))
list1 = []

     #list 串列
for i in range(a):
    b=input("輸入獎牌:").split()
    list1.append(b)
for j in list1:
    print(f'{j[0]}牌得到{j[1]}面')