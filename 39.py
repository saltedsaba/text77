#菱形迴圈練習 #已完成
a = int(input("請輸入:"))

e = a//2
g=(a-2)//2

for i in range(e+1,-1,-1):

  print(' '*i,'*'*(a-2*i),' '*i)

for i in reversed(range(g+1,0,-1)): 

  print(' '*i,'*'*(a-2*i),' '*i)