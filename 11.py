#星座查詢#已完成

a = list(map(int, input("請問月和日:").split()))

if a[0]==1:
    if a[1]>=21 and a[1]<=31:
        print("星座為:水瓶")
    else:
        print("星座為:魔羯")
elif a[0]==2:
    if a[1]>=19 and a[1]<=28:
        print("星座為:雙魚")
    else:
        print("星座為:水瓶")
elif a[0]==3:
    if a[1]>=21 and a[1]<=30:
        print("星座為:牡羊")
    else:
        print("星座為:雙魚")
elif a[0]==4:
    if a[1]>=21 and a[1]<=30:
        print("星座為:金牛")
    else:
        print("星座為:牡羊")
elif a[0]==5:
    if a[1]>=22 and a[1]<=31:
        print("星座為:雙子")
    else:
        print("星座為:金牛")
elif a[0]==6:
    if a[1]>=22 and a[1]<=30:
        print("星座為:巨蟹")
    else:
        print("星座為:雙子")
elif a[0]==7:
    if a[1]>=23 and a[1]<=31:
        print("星座為:獅子")
    else:
        print("星座為:巨蟹")
elif a[0]==8:
    if a[1]>=24 and a[1]<=31:
        print("星座為:處女")
    else:
        print("星座為:獅子")
elif a[0]==9:
    if a[1]>=24 and a[1]<=30:
        print("星座為:天平")
    else:
        print("星座為:處女")
elif a[0]==10:
    if a[1]>=24 and a[1]<=31:
        print("星座為:天蠍")
    else:
        print("星座為:天平")
elif a[0]==11:
    if a[1]>=23 and a[1]<=30:
        print("星座為:射手")
    else:
        print("星座為:天蠍")
elif a[0]==12:
    if a[1]>=22 and a[1]<=31:
        print("星座為:魔羯")
    else:
        print("星座為:射手")