#QT6.Write a program to calculate profit or loss.

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")