a = input("輸入一組四位數為：")
ls = []
for i in range(0,len(a)):
    ls.append(str((int(a[i])+7)%10))
astr = ""
print("輸出加密後的數字為：%s%s%s%s" %(ls[2] , ls[3] , ls[0] , ls[1]))