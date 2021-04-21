s = input("請輸入字元為：")
if not s:
    print("輸入為空！")
    s = input("請重新輸入字元為：")
a = len(s)
i = 0
count = 1
while i <= (a/2):
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break
if count == 1:
    print("YES")
else:
    print("NO")