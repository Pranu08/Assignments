#QT1.Python Program to Replace all Occurrences of ‘a’ with $ in a String

# Replace all occurrences of 'a' with '$'

string = input("Enter a string: ")

new_string = string.replace('a', '$')

print("String after replacement:", new_string)

#Without using replace()

string = input("Enter a string: ")

new_string = ""

for char in string:
    if char == 'a':
        new_string += '$'
    else:
        new_string += char

print("String after replacement:", new_string)