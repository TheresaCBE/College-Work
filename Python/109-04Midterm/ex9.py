s1 = input("輸入s1為：")
s2 = input("輸入s2為：")
a,b="",""
if len(s1) > len(s2):
    a=s1
    b=s2
elif len(s1) < len(s2):
    b=s1
    a=s2
elif len(a)==len(b):
    print("YES")
for i in range(0,len(a)-len(b)):
    ct = 0
    for j in range(i,len(b)+i):
        if b[j-i] == a[j]:
            ct+=1
    if len(b) == ct:
        print("YES")
        break
    else:
        print("NO")