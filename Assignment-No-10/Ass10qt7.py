#QT7.Write a program to create a new list from existing list which contains cube of
#each number of list.

# Program to create a new list containing cubes

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

cube_list = []

for i in range(n):
    cube = lst[i] * lst[i] * lst[i]
    cube_list.append(cube)

print("Original list =", lst)
print("Cube list =", cube_list) 