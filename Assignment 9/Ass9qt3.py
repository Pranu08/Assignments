#QT3.Write a program to reverse a given number using recursive function.

# Recursive function to reverse a number
def reverse(num, rev=0):
    if num == 0:
        return rev

    digit = num % 10
    rev = rev * 10 + digit

    return reverse(num // 10, rev)


# Main program
num = int(input("Enter a number: "))

result = reverse(num)

print("Reverse of the number =", result)