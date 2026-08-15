#QT5.Write a program to find factorial using recursion.

# Recursive function to find factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


# Main program
n = int(input("Enter a number: "))

result = fact(n)

print("Factorial =", result)