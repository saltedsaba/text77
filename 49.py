#存取串列中元素 #已完成 

c=[]
list1 = []
b=input("輸入英文句子").split()
list1.append(b)
for i in list1[::-1]:
    c += i
print(c)
print(' '.join(reversed(c)))