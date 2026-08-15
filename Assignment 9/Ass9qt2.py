#QT2.Write a program to check if given number is Armstrong or not using recursive
#function.

def armstrong(n, digits):
    if n == 0:
        return 0

    digit = n % 10
    return (digit ** digits) + armstrong(n // 10, digits)


# Main program
num = int(input("Enter a number: "))

digits = len(str(num))
result = armstrong(num, digits)

if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")