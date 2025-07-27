#v shape using the numbers
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = 5
for y in range(1, n + 1):
    # Increasing numbers
    for x in range(1, y + 1):
        print(x, end="")

    # Spaces (2 * (n - y))
    space = 2 * (n - y)
    print(" " * space, end="")

    # Decreasing numbers
    for j in range(y, 0, -1):
        print(j, end="")
    
    print()
