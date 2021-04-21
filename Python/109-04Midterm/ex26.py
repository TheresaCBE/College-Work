ls = []
lsm=[]
a = input("請輸入正整數")
for i in range(0,len(a)):
    for j in range(0,len(a)-i):
        lsk=""
        for k in range(j,i+j+1):
            lsk+=a[k]
        ls.append(lsk)
for i in range(0,len(ls)):
    a,j = len(ls[i]),0
    count = 1
    while j <= (a/2):
        if ls[i][j] == ls[i][a-j-1]:
            count = 1
            j += 1
        else:
            count = 0
            break
    if count == 1:
        lsm.append(ls[i])
    else:
        pass
lsms=list(map(int,lsm)) #str list轉int list(排列才會正常)
print("最長回文數字子數列為：%s"%max(lsms))