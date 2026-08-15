#QT12.Write a program to create three lists of numbers, their squares
#and cubes

numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]
cubes = [n ** 3 for n in numbers]

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)