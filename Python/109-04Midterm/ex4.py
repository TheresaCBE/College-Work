#判斷象限
ba = int(input("X軸座標：")) 
bb = int(input("Y軸座標："))
lno = ((abs(ba)**2)+(abs(bb)**2))
if ba > 0 and bb > 0:
    print("該點在第一象限，離原點距離為根號%d" %lno)
elif ba < 0 and bb > 0:
    print("該點在第二象限，離原點距離為根號%d" %lno)
elif ba < 0 and bb < 0:
    print("該點在第三象限，離原點距離為根號%d" %lno)
elif ba > 0 and bb < 0:
    print("該點在第四象限，離原點距離為根號%d" %lno)
elif ba==0 and bb>0:
    print("該點位於上半平面Y軸上，離原點距離為根號%d" %lno)
elif ba==0 and bb<0:
    print("該點位下半平面Y軸上，離原點距離為根號%d" %lno)
elif ba>0 and bb==0:
    print("該點位於右半平面X軸上，離原點距離為根號%d" %lno)
elif ba<0 and bb==0:
    print("該點位於左半平面X軸上，離原點距離為根號%d" %lno)
elif ba==0 and bb==0:
    print("該點位於原點")
