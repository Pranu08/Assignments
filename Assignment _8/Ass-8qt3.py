#QT3.Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

#a. Sum of 1 + 2 + 3 + ... + n
def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

n = int(input("Enter n: "))
print("Sum =", sum_series(n))

#b. Sum of 1! + 2! + 3! + ... + n!
def sum_factorial(n):
    sum = 0
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact
    return sum

n = int(input("Enter n: "))
print("Sum =", sum_factorial(n))

#c. Sum of 1¹ + 2² + 3³ + ... + nⁿ
def sum_power(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum

n = int(input("Enter n: "))
print("Sum =", sum_power(n))