#代辦事項新增  #已完成 #33

dolist = []
while True:
    a = str(input("請輸入事項(若無事項，請輸入end)："))
    if a == "end":
        break
    else:
        dolist.append(a)

for i in range(len(dolist)):
    print(str(i+1)+"."+dolist[i])