#QT10.Write a program to find maximum and minimum element in a list.

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

maximum = lst[0]
minimum = lst[0]

for i in range(1, n):
    if lst[i] > maximum:
        maximum = lst[i]

    if lst[i] < minimum:
        minimum = lst[i]

print("Maximum element =", maximum)
print("Minimum element =", minimum)