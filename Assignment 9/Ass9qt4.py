#QT4.Write a program to find sum of n numbers using recursion.

# Recursive function to find sum
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


# Main program
n = int(input("Enter the value of n: "))

result = sum_n(n)

print("Sum of first", n, "numbers =", result)