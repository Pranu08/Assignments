#QT11.WAP to check if a given number is Armstrong number or not. For
#each task create separate functions.

def is_armstrong(n):
    original = n
    digits = len(str(n))
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10

    return sum == original


n = int(input("Enter a number: "))

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")