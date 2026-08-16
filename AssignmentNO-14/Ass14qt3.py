#QT3.Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

# Python program to find unique words and their frequency
# using the set data type

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Find unique words using set
unique_words = set(words)

# Count frequency of each unique word
for word in unique_words:
    count = words.count(word)
    print(word, ":", count)