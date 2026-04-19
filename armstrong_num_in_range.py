till = 500
for num in range(1, till +1):
    digits = len(str(num))
    total = 0
    for i in str(num):
        total += int(i) ** digits
    if total == num:
        print(num)