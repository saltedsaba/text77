#已完成 #期末成績
chi = int(input("國文:"))
en = int(input("英文:"))
ma = int(input("微積分:"))
jo = int(input("體育:"))
e = int(input("程式設計:"))

#平均
avg = (chi + en + ma + jo + e)/5
print("平均分數 : ",avg)

#最高分
if chi>en:
    if chi > ma:
        if chi > jo:
            if chi > e:
                print("最高分科目 : 國文")
else:
    if en > ma:
        if en > jo :
            if en > e:
                print("最高分科目 : 英文")
    else:
        if ma > jo :
            if ma > e:
                print("最高分科目 : 微積分")
        else :
            if jo > e:
                print("最高分科目 : 體育")
            else:
                print("最高分科目 : 程式設計")

#最低分
if chi < en:
    if chi < ma:
        if chi < jo :
            if chi < e:
                print("最低分科目 : 國文")
else:
    if en < ma:
        if en < jo :
            if en < e:
                print("最低分科目 : 英文")
    else:
        if ma < jo :
            if ma < e:
                print("最低分科目 : 微積分")
        else:
            if jo < e:
                print("最低分科目 : 體育")
            else:
                print("最低分科目 : 程式設計")
