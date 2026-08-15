#QT10.Python Program to Take in Two Strings and Display the Larger String
#without Using Built-in Functions

# Display the larger of two strings without using built-in functions

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Find length of first string
count1 = 0
for char in string1:
    count1 += 1

# Find length of second string
count2 = 0
for char in string2:
    count2 += 1

# Compare lengths
if count1 > count2:
    print("Larger string:", string1)
elif count2 > count1:
    print("Larger string:", string2)
else:
    print("Both strings are of equal length.")