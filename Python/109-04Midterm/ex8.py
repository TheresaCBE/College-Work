a = int(input("輸入第一行正整數"))
b = input("第二行數列中數字為")
lsb = b.split(" ")
ctm = 0
mainpj=0
if len(lsb) != a:
    print("個數錯誤")
else:
    mainpj=1
    ls = []
    for i in range(0,a):
        ct = 0
        for j in range(0,a):
            if lsb[i] == lsb[j]:
                ct+=1
        ls.append(ct)
if mainpj==1:
    for i in ls:
        ctm+=i
    if ctm/len(ls) == 1:
        print("每個數字剛好只出現一次")
    else:
        lss=list(map(int,ls))
        lsss = sorted(lss , reverse=True)
        for i in range(0,a):
            if lsss[0] == int(ls[i]):
                print("最大出現次數的數字為%s\n出現次數為:%d" %(lsb[i],lsss[0]))
                break