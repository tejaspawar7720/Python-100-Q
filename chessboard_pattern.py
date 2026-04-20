num = 4
for i in range(num):
    for j in range(1,num+1):
        if (i+j) % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()
