num1 = 4
num2 = 6
for i in range(1, num1*num2+1):
    if i % num1 == 0 and i % num2 == 0:
        s= i
        break
print(s)
    