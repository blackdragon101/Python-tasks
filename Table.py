num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
greater_no = lambda no1,no2:no1 if no1>no2 else no2
# This is the way to handle condition in lambda function.Body first condition later.
number = int(greater_no(num1,num2))
specific_range = int(input("Enter the range of the table "))
def table(digit=number):
    """This is UDF that generates the table of a number which is greater out of the two no provided."""
    print("The table of the greater number is:")
    for i in range(1,specific_range+1):
        print(f"{number}^{i}={number*i}")
    return
print(table(number))







