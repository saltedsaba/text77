#顏色判斷 #已完成
ans = ["red","blue","red","green"]
a=input().split()
b=""
for j in range(10):
    for i in range(4):
        if a[i] in ans: #先判斷有沒有輸入題目的顏色
            if a[i] == ans[i]:
                b+="1"
            else:
                b+="2"
        else:
            b+="3"
    if b =="1111":
        print("正確答案")
        exit()
    else:
        print(b)
        b=""
        a = input().split()
print("挑戰失敗")