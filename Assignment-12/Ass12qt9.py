#QT9.Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String

# Calculate the number of words and characters in a string

string = input("Enter a string: ")

# Count characters
characters = 0
for char in string:
    if char != " ":
        characters += 1

# Count words
words = string.split()

print("Number of words:", len(words))
print("Number of characters:", characters)