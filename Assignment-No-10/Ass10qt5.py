#QT5.Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

# Program to search an element in a list

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

search = int(input("Enter the number to search: "))

count = 0

for i in range(n):
    if lst[i] == search:
        count = count + 1

if count > 0:
    print(search, "is present in the list.")
    print("It is present", count, "times.")
else:
    print(search, "is not present in the list.")