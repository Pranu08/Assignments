#QT9.Write a program to swap two numbers without using third variable.

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print(a, b)