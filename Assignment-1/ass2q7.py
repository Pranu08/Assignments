#QN.7) Program to find the Roots of a Quadratic Equation.
import math

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = b*b - 4*b*c

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =",x1)
print("Root 2 = ",x2)

