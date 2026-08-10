#QT11.Write a program to accept an intiger amount from user and tell minimum number of notes neede for representing that amount.

n = int(input("Enter amount:"))
notes = 0

for x in [500, 200, 100, 50, 20, 10]:
    notes += n // x 
    n %= x

print("Minimum notes=", notes)