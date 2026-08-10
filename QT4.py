#QT4.
area = float(input("Enter area of one wall:"))
inside = float(input("Enter interior cost:"))
outside = float(input("Enter exterior cost:"))

total = area * (inside + outside ) * 7

print("Total cost =", total)