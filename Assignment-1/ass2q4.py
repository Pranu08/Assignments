#QN.4) Write a program to enter P,T,R and calculate simple interest.

P = float(input("Enter Principal Amount:"))
T = float(input("Enter Time (in years):"))
R = float(input("Enter Rate of Interest:"))

SI = (P * T * R) / 100

print("Simple Interest=",SI) 
