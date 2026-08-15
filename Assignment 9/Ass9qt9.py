#QT9.Write a program to calculate the m to the power n using recursion.

# Recursive function to calculate m raised to power n
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)


# Main program
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

result = power(m, n)

print(m, "to the power", n, "=", result)