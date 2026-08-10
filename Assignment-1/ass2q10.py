#QN.10) write a program to calculate area of an equilateral triagle.

import math

side = float(input("Enter the side of the triangle:"))

area = (math.sqrt(3) / 4) * side * side

print("Area of equilateral triangle=",area)
