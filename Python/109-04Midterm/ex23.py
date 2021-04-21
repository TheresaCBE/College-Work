a=int(input("請輸入陣列大小："))
lsm,lsms,opstr=[],[],[]
for i in range(0,a):
    ai=input("")
    ls=ai.split(" ")
    lsm.append(ls)
for j in range(0,a):
    for k in range(0,a):
        lsms.append(int(lsm[j][k]))
lsms1=sorted(lsms,reverse=True)
for k in range(0,a):
    for j in range(0,a):
        if lsms1[0]==int(lsm[k][j]) or lsms1[1]==int(lsm[k][j]) or lsms1[2]==int(lsm[k][j]):
            opstr.append("(%d,%d)" %(k,j))
print("最大值為:%d\n位置為:%s,%s,%s" %(lsms1[0]+lsms1[1]+lsms1[2] , opstr[0],opstr[1],opstr[2]))