#QT8.H]

n = int(input("Enter n: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print("  " * (2 * (n - i) + 1), end="")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()