#QT5.Python Program to Sort a List According to the Length of the Elements
#within the list.

# Sort a list according to the length of its elements

words = ["apple", "cat", "banana", "dog", "elephant"]

# Sort using the length of each element
words.sort(key=len)

print("List sorted according to length:")
print(words)

#Using Bubble Sort

#If your assignment specifically requires Bubble Sort, use:

# Sort a list according to the length of its elements using Bubble Sort

words = ["apple", "cat", "banana", "dog", "elephant"]

n = len(words)

for i in range(n):
    for j in range(n - i - 1):
        if len(words[j]) > len(words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]

print("List sorted according to length:")
print(words)