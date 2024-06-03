# This is a python program to find whether a given sequence is palindrome or not.
number = input("Enter the number for which you want to do palindrome check ")
reverse = number[::-1]
if number == reverse:
    print("Yes, it is a palindrome")
else:
    print("No, it's not a palindrome")
