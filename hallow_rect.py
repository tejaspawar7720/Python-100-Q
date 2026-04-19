num = 4
num1 = 5
for i in range(num):
    for j in range(num1):
        if i == 0 or i == num - 1 or j == 0 or j == num1 - 1:
            print("*", end="")
        else:
            print(" ", end = "")
    print()