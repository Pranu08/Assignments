#QT7.F]

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i or j == n or i == 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()