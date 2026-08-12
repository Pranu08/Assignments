#QT3.Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter an alphabet:").lower()

if ch in "aeiou":
    print("vowel")
else:
    print("Consonant")    
