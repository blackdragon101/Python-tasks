user_string = input("Enter the string you want to invert: ")
def invert_string(string):
    if len(string) == 0:
        return string
    else:
        return invert_string(string[1:]) + string[0]
print(invert_string(user_string))
