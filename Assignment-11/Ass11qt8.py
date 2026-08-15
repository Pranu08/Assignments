#QT8.Print 1 to 100 in snakes and ladder pattern.

# Print 1 to 100 in Snakes and Ladders pattern

for row in range(10):
    start = row * 10 + 1
    end = start + 10

    if row % 2 == 0:
        # Left to right
        for num in range(start, end):
            print(num, end="\t")
    else:
        # Right to left
        for num in range(end - 1, start - 1, -1):
            print(num, end="\t")

    print()