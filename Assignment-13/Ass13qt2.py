#QT2.Python Program to Concatenate Two Dictionaries Into One


# Concatenate two dictionaries into one

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Add the second dictionary to the first
dict1.update(dict2)

print("First Dictionary:", {"a": 1, "b": 2})
print("Second Dictionary:", dict2)
print("Concatenated Dictionary:", dict1)