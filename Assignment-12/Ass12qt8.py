#QT8.Python Program to Remove the Characters of Odd Index Values in a
#String

# Remove characters of odd index values

string = input("Enter a string: ")

new_string = ""

for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]

print("String after removing odd index characters:", new_string)