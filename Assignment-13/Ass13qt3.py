#QT3.Python Program to Check if a Given Key Exists in a Dictionary or Not

# Check if a key exists in a dictionary

my_dict = {
    "name": "John",
    "age": 20,
    "city": "Pune"
}

key = input("Enter the key to search: ")

if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")