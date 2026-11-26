total = 0
while True:
    n = int(input("Enter a number:"))
    if n < 0:
        continue
    if n == 0:
        break
    total += n
    print("n is", n, "total is now", total)
print("Total:", total)