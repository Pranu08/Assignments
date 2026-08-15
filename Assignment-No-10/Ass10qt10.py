#QT10.Write a program to remove all occurrences of a given element in the list.

# Program to remove all occurrences of an element

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

element = int(input("Enter the element to remove: "))

new_list = []

for i in range(n):
    if lst[i] != element:
        new_list.append(lst[i])

print("Original list =", lst)
print("List after removing all occurrences =", new_list)