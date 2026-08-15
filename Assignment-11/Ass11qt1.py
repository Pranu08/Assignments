#QT1. Python Program to Put Even and Odd elements of a List into two Different
#Lists

# Program to separate even and odd elements

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

even_list = []
odd_list = []

for i in range(n):
    if lst[i] % 2 == 0:
        even_list.append(lst[i])
    else:
        odd_list.append(lst[i])

print("Original list =", lst)
print("Even elements =", even_list)
print("Odd elements =", odd_list)