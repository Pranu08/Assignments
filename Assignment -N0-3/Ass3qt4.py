#QT4.Write a program to input all sides of a triangle and check whether triangle is valid or
#not.

a = float(input("Enter side 1:"))
b = float(input("Enter side 2:"))
c = float(input("Enter side 3:"))

if a + b > c and b + c > a and c + a > b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")