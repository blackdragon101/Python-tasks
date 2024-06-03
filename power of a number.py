number = int(input("Enter the number: "))
power = int(input("Enter the power of the number: "))
def power_of_a_number(number,power):
    if power == 0:
        return 1
    else:
        return number * power_of_a_number(number,power-1)
print(power_of_a_number(number,power))
