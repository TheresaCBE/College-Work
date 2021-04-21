#找出共同字
lista = "紅豆生南國，春來發幾枝？願君多采擷，此物最相思。"
listb = "春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
lsa=lista.replace("，","")
lsa1=lsa.replace("。","")
lsa2=lsa1.replace("？","")
lsb=listb.replace("，","")
lsb1=lsb.replace("。","")
print(set(lsa2)&set(lsb1))