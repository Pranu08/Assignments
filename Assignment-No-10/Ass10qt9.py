#QT9.Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)

print("Even elements =", even)
print("Odd elements =", odd)