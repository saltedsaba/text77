#提款機搜尋 #已完成

b=[]
a =int(input("請輸入查詢組數N為："))
for i in range(a):
    b.append(input("第%s組為:" %(i+1)).split(" "))

    if b[0][0] =="123":
        if b[0][1] =="456":
            print("9000")
        else:
            print("error")
    elif b[0][0] =="456":
        if b[0][1] =="789":
            print("5000")
        else:
            print("error")
    elif b[0][0] =="789":
        if b[0][1] =="888":
            print("6000")
        else:
            print("error")
    elif b[0][0] =="336":
        if b[0][1] =="558":
            print("10000")
        else:
            print("error")
    elif b[0][0] =="775":
        if b[0][1] =="666":
            print("12000")
        else:
            print("error")
    elif b[0][0] =="566":
        if b[0][1] =="221":
            print("7000")
        else:
            print("error")
    else:
        print("error")
    b.clear()
