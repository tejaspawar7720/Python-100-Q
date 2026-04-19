n = 9474
digits = len(str(n))
total = 0
for i in str(n):
    total += int(i) ** digits
if total == n:
    print("Armstrong")