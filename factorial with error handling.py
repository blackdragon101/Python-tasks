# This is an exception handling program for factorial.
try:
    number = int(input("Enter the number: "))
    assert isinstance(number,int),"The number must not be a string"
    assert number>1,f"The {number} is less than 1, can't take factorial of negative integers"
    factorial = 1
    if number == 1:
        print(f"The factorial of number is 0")
except AssertionError as a:
    print(a)
    number = int(input("Enter the number: "))
except ValueError as v:
    print(v)
    number = int(input("Enter the number: "))
else:
    for i in range(1,number+1):
        factorial = factorial *i
        print(f"The factorial of {number} is {factorial}")











