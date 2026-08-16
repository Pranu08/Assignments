#QT3.Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

# Python program to find two numbers whose product
# is maximum among all pairs using Python set

numbers = [2, 3, 5, 7, 9, 10]

# Convert the list into a set
num_set = set(numbers)

max_product = None
max_pair = None

# Check all possible pairs
for x in num_set:
    for y in num_set:
        if x != y:
            product = x * y

            if max_product is None or product > max_product:
                max_product = product
                max_pair = (x, y)

print("Two numbers:", max_pair)
print("Maximum product:", max_product)