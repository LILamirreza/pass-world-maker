import random
import string
import os
os.system("cls")


print ("hello, welcome to my password generator :")
user_email = input("enter your email : ")
password_length = int(input("enter password length :"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string. punctuation
characters = lower + upper + num + symbols


email_name = user_email[:user_email.index("@")]


length = password_length - len(email_name)
temp = random.sample(characters, length)

                         
password = email_name + ''.join(temp)

                         
print("\npassword :", password, end = "\n\n\n")
