
from itertools import count
#字元出現次數 #已完成

a = str(input("檢測的字元:"))
b = str(input("檢測的單一字元:"))
count = a.count(b)
print("字元",b,"出現次數為:",count)