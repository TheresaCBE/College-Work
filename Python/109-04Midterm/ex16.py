alm , blm = [],[]
a=input("a")
al = a.split(" ")
for i in range(0,int(al[0])):
    ain=input("")
    alm.append(ain.split(" "))
b=input("b")
bl = a.split(" ")
for j in range(0,int(bl[0])):
    bin=input("")
    blm.append(bin.split(" "))
if a[0]==b[0] and a[1]==b[1]:
    for k in range(0,int(al[0])):
        lsm = []
        for l in range(0,int(al[1])):
            lsm.append(str(int(alm[k][l])+int(blm[k][l])))
        print(" ".join(lsm))
else:
    print("兩個矩陣無法相加")