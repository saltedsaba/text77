#座標判斷及原點距離計算 #已完成

X=int(input("請輸入X座標的位置:"))
Y=int(input("請輸入Y座標的位置:"))

if X>0 and Y>0:
    print("該點位於第一象限，離原點距離為根號",(X**2+Y**2))
elif X>0 and Y<0:
    print("該點位於第四象限，離原點距離為根號",(X**2+Y**2))
elif X<0 and Y<0:
    print("該點位於第三象限，離原點距離為根號",(X**2+Y**2))
elif X<0 and Y>0:
    print("該點位於第二象限，離原點距離為根號",(X**2+Y**2))
elif X==0 and Y==0:
    print("該點位於原點")
elif X==0 and Y<0:
    print("該點位於下半平面Y軸上，離原點距離為根號",(X**2+Y**2))
elif X==0 and Y>0:
    print("該點位於上半平面Y軸上，離原點距離為根號",(X**2+Y**2))
elif X>0 and Y==0:
    print("該點位於右半平面X軸上，離原點距離為根號",(X**2+Y**2))
elif X<0 and Y==0:
    print("該點位於左半平面X軸上，離原點距離為根號",(X**2+Y**2))    