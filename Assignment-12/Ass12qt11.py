#QT11.Python Program to replace every blank space with hyphen in a string.

# Replace every blank space with a hyphen

string = input("Enter a string: ")

new_string = ""

for char in string:
    if char == " ":
        new_string += "-"
    else:
        new_string += char

print("String after replacing spaces with hyphens:", new_string)