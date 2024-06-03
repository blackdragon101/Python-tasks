# This is a python program to generate a random password.
import random
characters = ''
length = int(input("Enter the length of the password "))
up = input("Do you want to include uppercase letters? Y/N ")
low = input("Do you want to include lower case letters? Y/N ")
dig = input("Do you want to include digits in the password? Y/N ")
sc = input("Do you wish to include special characters in your password? Y/N ")
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '123456789'
special = '@/!&*%$*#|><()'
if up == 'Y':
    characters+= upper
if low == 'Y':
    characters+= lower
if dig == 'Y':
    characters+= digits
if sc == 'Y':
    characters += special
password = ''.join(random.sample(characters,length))
print(f"Your generated password is:{password}")
