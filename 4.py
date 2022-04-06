#座標判斷及計算離原點距離
import math


x=float(input("請輸入x座標"))
y=float(input("請輸入y座標"))
if x>0 and y>0:
    Distance=(x-0)**2+(y-0)**2
    print("第I象限")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
elif x<0 and y>0:
    Distance=(x-0)**2+(y-0)**2
    print("第II象限")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
elif x<0 and y<0:
    Distance=(x-0)**2+(y-0)**2
    print("第III象限")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
elif x>0 and y<0:
    Distance=(x-0)**2+(y-0)**2
    print("第IV象限")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
elif x==0 and (y<0 or y>0):
    Distance=(x-0)**2+(y-0)**2
    print("Y軸上")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
elif y==0 and (x<0 or x>0):
    Distance=(x-0)**2+(y-0)**2
    print("X軸上")
    print("離原點距離為根號 %.0f" %(math.ceil(Distance)))
else:
    print("在原點")