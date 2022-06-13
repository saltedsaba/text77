list1 = [1, 2, 4]
list2 = [3, 4, 5]

set1 = set(list1) # 将列表转换成集合
set2 = set(list2)

print(set1 & set2) # 相同元素
print(set1 ^ set2) # 不同元素
