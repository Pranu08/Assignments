#Qt.1 write a program to find the area and perimeter of the following figure accept the length breadth and radius form user
l = float(input("Length"))
b = float(input("Breadth")) 
r = float(input("Radius"))

area = l * b + 3.14 * r * r /2
perimeter = 2 * l + b + 3.14 * r

print("Area=", area)
print("Perimeter=", perimeter)