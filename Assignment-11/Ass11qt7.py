#QT7.Python Program to Find the Intersection of Two Lists

# Find the intersection of two lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find intersection using set
intersection = list(set(list1) & set(list2))

print("First List:", list1)
print("Second List:", list2)
print("Intersection of two lists:", intersection)