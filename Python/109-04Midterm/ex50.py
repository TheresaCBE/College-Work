b = input("剔除重復的字")
lsa=b.replace("，","")
lsa1=lsa.replace("。","")
lsa2=lsa1.replace("？","")
lsam=[]
for i in range(0,len(lsa2)):
    ct=0
    for j in lsa2:
        if lsa2[i]==j:
            ct+=1
    if ct>=2:
        lsam.append(lsa2[i])
set(lsam)