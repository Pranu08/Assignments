#QT6.Python Program to Find the Union of two Lists

# Find the union of two lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find union using set
union = list(set(list1) | set(list2))

print("First List:", list1)
print("Second List:", list2)
print("Union of two lists:", union)