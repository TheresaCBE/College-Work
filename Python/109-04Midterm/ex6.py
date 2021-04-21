a = input("輸入值為")
al = a.split(",")
ls = sorted(al , reverse=True)
lsa = sorted(al , reverse=False)
sa , sb = "",""
for i in range(0,len(al)):
    sa +=ls[i]
    sb +=lsa[i]
print(int(sa)-int(sb))