# This is a python program to handle any exceptions in conversion of decimal to hex value.
def Hexadecimal():
    try:
        number = int(input("Enter the decimal number which you want to convert to hexadecimal value: "))
        assert isinstance(number,int),f"The number {number} is a string,can't convert"
        hexa = hex(number)
        print(f"The hexadecimal value of decimal number{number} is {hexa}"),
    except AssertionError as asserion:
        print(asserion)
        number = int(input("Enter the decimal number which you want to convert to hexadecimal value: "))
    except ValueError as value:
        print(value)
        number = int(input("Enter the decimal number which you want to convert to hexadecimal value: "))
    except TypeError as type:
        print(type)
        number = int(input("Enter the decimal number which you want to convert to hexadecimal value: "))
    finally:
        print("UDF called successfully")
Hexadecimal()

