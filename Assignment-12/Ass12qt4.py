#QT4.Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged

# Exchange the first and last character of a string

string = input("Enter a string: ")

if len(string) <= 1:
    new_string = string
else:
    new_string = string[-1] + string[1:-1] + string[0]

print("New string:", new_string)