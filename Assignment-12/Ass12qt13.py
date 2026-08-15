#QT13.Python Program to count number of digits and letters in a string.

# Count the number of digits and letters in a string

string = input("Enter a string: ")

digits = 0
letters = 0

for char in string:
    if char >= '0' and char <= '9':
        digits += 1
    elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letters += 1

print("Number of digits:", digits)
print("Number of letters:", letters)