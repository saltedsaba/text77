#兩數差值 #完成

#list1 = list(map(int, input("輸入值為:").split(",")))
#list2 = list1


#number1=map(int,list1.sort()) #由小排到大
#number2=map(int,list2.reverse()) #由大到小

from posixpath import split


str1 = list(input("請輸入0~92的N個數，0<N<8:").split(","))
if len(str1)>7:
    print("輸入錯誤，請重新輸入")
    str1 = list(input("請輸入0~92的N個數，0<N<8:").split(","))
else:
    int1 = list(map(int,str1))
    int1.sort()

    int2 = int1.copy()
    int2.reverse()
    list3=[]
    c=0
    for i in range(len(int1)):
        int1val = int1[i]
        int2val = int2[i]
        if int2val>=int1val:
            c=int2val-int1val
        else:
            c=10-int1val+int2val
            list3[i-1]-=1
            if list3[i-1] == -1:
                list3[i-1] =9
                list3[i-2] -=1
        list3.append(c)
    print("最大數列與最小數列差值為",end="") #end="" 是數字不空行
    for i in range(len(list3)):
        print(list3[i],end="")


