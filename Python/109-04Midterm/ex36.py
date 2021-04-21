#演算法練習
a=int(input("整數n:"))
ls=[a]
while a!=1:
    if a%2!=0:
        a=a*3+1
        ls.append(a)
    else:
        a//=2
        ls.append(a)
print("數列:"," ".join(list(map(str,ls))))
print("cycle length:%d"%len(ls))