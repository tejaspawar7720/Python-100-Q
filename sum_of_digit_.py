num =9087
count = 0
while num > 0:
    count += num % 10
    num //= 10
    print(count)

