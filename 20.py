#電影票購買計算 
a = int(input("組數為:"))
b = []
c = []
for i in range(a):
    b = input("第"+str(i+1)+"組為:").split(" ")
    c.append("第"+str(i+1)+"組應收費用:"+str(250*int(b[0])+175*int(b[1])))
for i in range(a):
    print(c[i])