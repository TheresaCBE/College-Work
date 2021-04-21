from math import *
aj = int(input("幾層?"))
for i in range(0, ceil((aj+1)/2)):
    print(" "*(6-i)+"*"*i+"*"*(i-1))
for j in range(ceil((aj+1)/2),0,-1):
    print(" "*(6-j)+"*"*j+"*"*(j-1))