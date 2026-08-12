# #QT1.Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

userid = "admin"
password = "1234"

for i in range(3):
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")

    if uid == userid and pwd == password:
        print("Login Successful")
        break
    else:
        print("Incorrect User ID or Password")

else:
    print("3 attempts completed. Program terminated.")