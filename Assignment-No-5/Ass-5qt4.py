#QT4. WAP to print Armstrong number within a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    temp = num
    total = 0
    n = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10

    if total == num:
        print(num)