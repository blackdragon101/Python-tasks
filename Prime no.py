num = int(input('Enter the number '))
value = False
for divisor in range(2,num):
    if num % divisor == 0:
        value = True
        break
if value:
    print('not a prime')
else:
    print('prime')































