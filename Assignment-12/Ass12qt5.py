#QT6.Python Program to Count the Number of Vowels in a String

# Count the number of vowels in a string

string = input("Enter a string: ")

count = 0

for char in string:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)