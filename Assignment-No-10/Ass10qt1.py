#QT10.Write a program to find sum of all elements of list
#(without using inbuilt functions)

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

total = 0

for i in range(n):
    total = total + lst[i]

print("Sum of all elements =", total)