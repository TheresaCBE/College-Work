ls = []
lsm=[]
a = input("請輸入正整數")
for i in range(0,len(a)):
    for j in range(0,len(a)-i):
        lsk=""
        for k in range(j,i+j+1):
            lsk+=a[k]
        ls.append(lsk)

for j in ls:
    c = 2
    while c < int(j):
        if int(j) % c == 0:
            break
        c += 1
    if c == int(j):
        lsm.append(int(j))
try:
    print("最大的質數值為：%s" %(max(lsm)))
except:
    print("最大的質數值為：No prime found")