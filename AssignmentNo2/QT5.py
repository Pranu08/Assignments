#QT5. WAP to calculate selling price of book based on cost price and discount.

cost = float(input("Enter cost price:"))
discount = float(input("Enter discount %:"))

selling_price = cost - (cost * discount / 100)

print("Selling Price =", selling_price)