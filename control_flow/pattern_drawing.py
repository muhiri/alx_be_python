size = int(input("Enter the size of the pattern: "))
print("size =", size)
row = 1
while row <= size:
    for i in range(size):
        print("*", end="")
    print()
    row += 1
    