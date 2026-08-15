#QT13.Write a program to print list after removing even numbers.

# Program to remove even numbers from a list

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

new_list = []

for i in range(n):
    if lst[i] % 2 != 0:
        new_list.append(lst[i])

print("Original list =", lst)
print("List after removing even numbers =", new_list)