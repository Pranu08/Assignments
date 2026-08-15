#QT11.Write a program to print all numbers which are divisible by m and n in the
#list.

# Program to print numbers divisible by both m and n

size = int(input("Enter the number of elements: "))

lst = []

for i in range(size):
    value = int(input("Enter element: "))
    lst.append(value)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Numbers divisible by both", m, "and", n, "are:")

for i in range(size):
    if lst[i] % m == 0 and lst[i] % n == 0:
        print(lst[i], end=" ")