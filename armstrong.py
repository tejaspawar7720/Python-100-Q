n = 153
total = 0
for i in str(n):
    total += int(i) ** 3
if total == n:
    print("Armstrong")