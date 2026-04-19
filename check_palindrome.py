num = 121
on = num
rn = 0
while num != 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10
print(rn)
if rn == on:
    print("Its palindrome") 
else:
    print("Not palindrome")  