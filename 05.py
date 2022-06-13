#階層判斷 #已完成
a=int(input("請輸入一正整數:"))

total=1
t=1

while total<=a:
    total*=t
    t+=1
print("超過a的最小階層為:",t-1)