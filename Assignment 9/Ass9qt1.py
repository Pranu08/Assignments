#QT1.Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

# Recursive function to find factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

# Recursive function to find sum of factorials
def sum(n):
    if n == 0:
        return 0
    return fact(n) + sum(n - 1)

# Main program
n = int(input("Enter the value of n: "))

result = sum(n)

print("Sum of the series =", result)