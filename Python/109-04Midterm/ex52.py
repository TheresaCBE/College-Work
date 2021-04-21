lsna ,lsma,lsdo = [],[],[] 
a=int(input("輸入n值:"))
for i in range(0,a):
    name = input("請輸入姓名：") 
    mail = input("請輸入電郵：")
    lsna.append(name)
    lsma.append(mail.split("@")[0])
    lsdo.append(mail.split("@")[1])
main = input("請輸入要查找的使用者名稱：")
idm = lsna.index(main)
print(main,"電子郵件帳號為",lsma[idm],"@",lsdo[idm] , sep="")