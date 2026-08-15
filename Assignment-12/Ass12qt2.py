#QT2.Python Program to Remove the nth Index Character from a Non-Empty
#String

# Remove the nth index character from a string

string = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

new_string = string[:n] + string[n + 1:]

print("String after removing character:", new_string)