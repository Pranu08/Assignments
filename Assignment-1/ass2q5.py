#QN.5) Write a program to enter P,T,R and calculate compound interest

P = float(input("Enter Principal Amount:"))
T = float(input("Enter Time (in years):"))
R = float(input("Enter Rate of Interest:"))

A = P * (1 + R / 100) ** T 
CI = A - P

print("Compound Interest =",CI)
print("Total Amount =",A)