mi = int(input("請輸入Ｍ？"))
sd = 1
smd = 1
while smd <= mi:
    smd *= sd
    sd += 1
print("超過M為%d的最小階乘N值為：%d" % (mi , sd-1))