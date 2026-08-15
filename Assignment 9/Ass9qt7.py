#QT7.Write a program to find sum of digits using recursion.

# Recursive function to find sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


# Main program
n = int(input("Enter a number: "))

result = sum_digits(n)

print("Sum of digits =", result)