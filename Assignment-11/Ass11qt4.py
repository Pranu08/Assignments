#QT4.Python Program to Find the Second Largest Number in a List Using Bubble
#Sort

# Find the second largest number using Bubble Sort

numbers = [10, 5, 8, 20, 15]

# Bubble Sort
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# The list is now sorted in ascending order
print("Sorted list:", numbers)

# Second largest number
second_largest = numbers[-2]

print("Second largest number:", second_largest)