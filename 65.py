#共通好友數量判斷 #已完成 
b=set(input("輸入A的朋友").split())

c=set( input("輸入B的朋友").split())
print(len(b&c))