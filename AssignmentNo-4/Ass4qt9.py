#QT9.WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter start: "))
end = int(input("Enter end: "))
n = int(input("Enter number: "))

for i in range(start, end + 1):
    if i % n == 0:
        print(i)