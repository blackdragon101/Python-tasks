num = int(input('Enter the number '))
factorial = 1
if num < 0:
    print('sorry, factorial of a neg no does not exist')
if num == 0:
    print('Factorial of 0 is 1')
if num > 0:
    # We increase the value of i from 1 to that number and multiply it with the factorial we get on left.
    for i in range(1,num + 1):
        factorial *= i
    print(factorial)
# This is python program to find the factorial.




