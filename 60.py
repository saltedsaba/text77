#母音替換 #已完成 
mu=["a","e","i","o","u"]
b=""
a=(input("請輸入一串小寫英文:"))

for i in a:
    if i in mu:
        b = b + "."
    else:
        b = b + i

print(b)