#QT5.Sum of all prime numbers between 1 to n

def sum_prime(n):
    sum = 0

    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            sum = sum + num

    return sum

n = int(input("Enter n: "))
print("Sum of prime numbers =", sum_prime(n))