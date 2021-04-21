import numpy as np
ai,ai2=input(""),input("")
ary = np.array([list(map(int,ai.split(" "))),list(map(int,ai2.split(" ")))])
ary_inv = np.linalg.inv(ary)
for i in range(0,2):
    for j in ary_inv[i]:
        print(round(j,1),end=" ")
    print("\n")