num = 4
for i in range(num+1):
    for j in range(num):
        if (i+j) % 2 == 0:
            print(1,end="")
        else:
            print(0, end="")
    print()