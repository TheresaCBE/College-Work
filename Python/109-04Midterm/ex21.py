datals = [["123","456",9000],["456","789",5000],["789","888",6000],["336","558",10000],["775","666",12000],["566","221",7000]]
a = int(input("輸入查詢組數N為："))
for i in range(0,a):
    ais=[]
    ct=0
    ai = input("")
    ais = ai.split(" ") 
    for i in range(0,len(datals)):
        if ais[0] == datals[i][0] and ais[1] == datals[i][1]:
            ct+=1
            print(datals[i][2])
            break
        else:
            pass
    if ct==0:
        print("error")