#孿生質數 #已完成 #28
a=int(input("請輸入第一個判斷的數字:"))
b=int(input("請輸入第二個判斷的數字:"))

if  b-a > 2 or b-a < 2:
    print("N")
else:
    if a % 2 > 0 or a%2 <0:

        if b % 2 > 0 or b%2 <0:
            print("Y")
        else:
            print("N")
    else:
        print("N")
