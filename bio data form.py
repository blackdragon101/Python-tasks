# This is a bio data form with error handling.
try:
    name = input("Enter your name: ")
    assert name.isalpha(),"You must enter a string"
except AssertionError as a:
    print(a)
    name = input("Enter your name: ")
try:
    address = input("Enter your address: ")
    assert len(address)>3,"You entered an invalid address"
except AssertionError as b:
    print(b)
    address = input("Enter your address: ")
try:
    contact = input("Enter your contact number: ")
    assert contact.isdigit(),"The contact number you entered has alphabets in it"
except AssertionError as c:
    print(c)
    contact = input("Enter your contact number: ")
try:
    gender1 = input("Enter your Gender(Male/Female): ")
    gender2 = gender1.lower()
    assert gender2 == 'male' or gender2 =="female", "You entered wrong gender"
except AssertionError as d:
    print(d)
    gender1 = input("Enter your Gender(Male/Female): ")
try:
    age = int(input("Enter your age: "))
    assert 0<age<150, "You entered an invalid age."
except AssertionError as e:
    print(e)
    age = int(input("Enter your age: "))





