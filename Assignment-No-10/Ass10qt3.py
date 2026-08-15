#QT3.Write a program to find the second largest element in the list.

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

largest = lst[0]
second_largest = lst[0]

for i in range(1, n):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]

print("Second largest element =", second_largest)