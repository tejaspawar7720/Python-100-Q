num = 1205
rn = 0
while num != 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10
print(rn)