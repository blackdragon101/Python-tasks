def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)
print("The fibonacci series with first 20 terms is:")
for i in range(20):
    print("",fib(i),end='')




