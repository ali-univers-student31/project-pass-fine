import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

x=input("Enter the your password to hacked in my hand :   ")
while True:
    password = ''.join(random.choices(characters,k=len(x)))
    if password==x:
        print(f"Your password is: {password}")
        inp = input("Do you agree with password. Press Y or N - ")
        if inp == "Y":
            print("Password was found!")
            break 

