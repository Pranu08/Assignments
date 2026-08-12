# #QT2.Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter number of students: "))
percentages = []

for i in range(n):
    print("Student", i + 1)
    total = 0

    for j in range(5):
        marks = float(input("Enter marks: "))
        total += marks

    percentage = total / 5
    percentages.append(percentage)

print("\nPercentages of students:")
for p in percentages:
    print(p, "%")

average = sum(percentages) / n
print("Average percentage =", average, "%")