#QT14.Python Program to count the occurrences of ach word in a string.

# Count the occurrences of each word in a string

string = input("Enter a string: ")

words = string.split()
counted = []

for word in words:
    if word not in counted:
        count = 0

        for w in words:
            if w == word:
                count += 1

        print(word, ":", count)
        counted.append(word)