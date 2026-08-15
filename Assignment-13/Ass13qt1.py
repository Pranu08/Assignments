#QT1.Python Program to Add a Key-Value Pair to the Dictionary

# Add a key-value pair to a dictionary

my_dict = {
    "name": "John",
    "age": 20
}

key = input("Enter the key: ")
value = input("Enter the value: ")

my_dict[key] = value

print("Dictionary after adding key-value pair:")
print(my_dict)