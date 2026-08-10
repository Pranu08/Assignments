#QT3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter feet:"))
inches = float(input("Enter inches:"))

cm = (feet * 30.45) + (inches * 2.54)

print("Meter =", cm / 100)
print("Centimeter=", cm)