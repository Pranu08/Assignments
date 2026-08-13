#QT6.E]

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    if i == 1:
        print(1)
    elif i == n:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
        print(1, end="")
        print(" " * (2 * i - 3), end="")
        print(i)