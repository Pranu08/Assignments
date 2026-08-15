#QT8.Write a program to create a duplicate of an existing list. It should not point to
#same list.

# Program to create a duplicate of an existing list

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

# Create a separate duplicate list
duplicate = []

for i in range(n):
    duplicate.append(lst[i])

print("Original list =", lst)
print("Duplicate list =", duplicate)

# Modify duplicate list
duplicate[0] = 100

print("After modifying duplicate list:")
print("Original list =", lst)
print("Duplicate list =", duplicate)