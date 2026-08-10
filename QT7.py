#QT7. Find the sum of three degit number

num = int(input("Enter 3 degit number:"))

sum = num // 100 + (num // 10) % 10 + num % 10

print("Sum:",sum)