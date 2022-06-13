#製作電子郵件通訊錄 #已完成 #20
a=int(input("請輸入n:"))
dict1 = {}
for i in range(a):
    b = input("輸入姓名:")
    c = input("輸入電子郵件")
    dict1[b] = c

j = str(input("輸入查詢用戶"))

print(f'{j}的電子郵件為{dict1[j]}')