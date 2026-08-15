#QT3.# Python Program to Sort the List According to the Second Element in Sublist

# Program to sort list according to the second element

lst = [[1, 30], [2, 10], [3, 20], [4, 5]]

print("Original list =", lst)

# Sort according to the second element
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i][1] > lst[j][1]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print("List after sorting =", lst)