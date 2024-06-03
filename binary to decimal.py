# This is a python program to convert binary to decimal.
binary_num = (input("Enter the binary number "))
length = len(binary_num) - 1
sum = 0
for digit in binary_num:
    number = int(digit) *(2**length)
    sum = sum + number
    length -= 1
print(f"The number in decimals is: {sum}" )








