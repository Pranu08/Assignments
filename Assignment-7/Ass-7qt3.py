#QT3. C]

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i == 1:
        print(1)
    elif i == n:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
        print(1, end=" ")
        print("  " * (i - 2), end="")
        print(i)