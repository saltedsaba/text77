#輸入年份，判斷生肖  #已完成
a=int(input("請輸入西元年份"))

if a<0:
    if a%12==9:
        print("rat")
    elif a%12==8:
        print("ox")
    elif a%12==7:
        print("tiger")
    elif a%12==6:
        print("rabbit")
    elif a%12==5:
        print("dragon")
    elif a%12==4:
        print("snake")
    elif a%12==3:
        print("horse")
    elif a%12==2:
        print("sheep")
    elif a%12==1:
        print("monkey")
    elif a%12==0:
        print("rooster")
    elif a%12==11:
        print("dpg")
    elif a%12==10:
        print("pig")
else :
    if a%12==4:
        print("rat")
    elif a%12==5:
        print("ox")
    elif a%12==6:
        print("tiger")
    elif a%12==7:
        print("rabbit")
    elif a%12==8:
        print("dragon")
    elif a%12==9:
        print("snake")
    elif a%12==10:
        print("horse")
    elif a%12==11:
        print("sheep")
    elif a%12==0:
        print("monkey")
    elif a%12==1:
        print("rooster")
    elif a%12==2:
        print("dpg")
    elif a%12==3:
        print("pig")