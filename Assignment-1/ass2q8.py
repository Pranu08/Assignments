#QN.8) Write a program to convert days into years,weeks,and days.

days = int(input("Enter number of days:"))

years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print("Year =",years)
print("weeks=",weeks)
print("Days=",days)
