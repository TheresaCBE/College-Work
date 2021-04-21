#簡化生肖查詢
lse1 = ["雞", "狗", "豬", "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴"]
lsei = int(input("輸入年分："))
for i in range(0, 11):
    if lsei % 12 == i+1:
        print(lse1[i])