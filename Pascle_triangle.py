import math
num = 5
for i in range(num+1):
    for j in range(i+1):
        print(math.comb(i,j) , end="")
    print()