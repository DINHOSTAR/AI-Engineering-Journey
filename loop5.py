for row in range(1, 6):
    for col in range(1, 6):
        print( col * row, end=" ")
    print()                         # 1*1 to 5*5

for row in range(1, 5):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()                         #Triangle