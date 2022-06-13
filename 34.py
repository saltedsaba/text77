#新公倍數  #已完成
a =  int(input("輸入一個正整數(11<=n<=1000)"))

if a >1000 or a < 11:
    print("請重新輸入")

elif a%2==0 and a%11==0:
    if a%5>0:
        if a%7>0:
            print("YES")
        else:
            print("NO")
    else:
        print("no")
else:
    print("NO")