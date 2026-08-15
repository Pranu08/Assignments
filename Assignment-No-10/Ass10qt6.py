#QT6.Write a program to remove duplicates from the list.

# Program to remove duplicates from a list

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

new_list = []

for i in range(n):
    found = False

    for j in range(len(new_list)):
        if lst[i] == new_list[j]:
            found = True
            break

    if found == False:
        new_list.append(lst[i])

print("Original list =", lst)
print("List after removing duplicates =", new_list)