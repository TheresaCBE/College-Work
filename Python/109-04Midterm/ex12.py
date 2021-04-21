a=input("輸入一整數序列為：")
al = a.split(" ")
ls=[]
for i in range(0,len(al)):
    ct = 0
    for j in range(0,len(al)):
        if al[i] == al[j]:
            ct+=1
    ls.append(ct)
cta = ls.index(max(ls))
if len(al)<max(ls)*2:
    print("過半元素為：%s" %al[cta])
elif len(al)>=max(ls)*2:
    print("過半元素為：NO")