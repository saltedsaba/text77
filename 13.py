#判斷是否回文#已完成
a=str(input("請輸入你的文字"))
s=a
B=(s[0:])
C=(s[::-1])
if B==C:
    print("YES")
else:
    print("NO")