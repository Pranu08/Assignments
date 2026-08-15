#QT4.Write a program to reverse the list.

# Program to reverse a list

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

print("Original list =", lst)

print("Reversed list =", end=" ")

for i in range(n - 1, -1, -1):
    print(lst[i], end=" ")