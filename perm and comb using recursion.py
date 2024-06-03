def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)
#  This is a factorial function using recursion.
def permutation(n,r):
    perm = factorial(n)/factorial(n-r)
    return int(perm)
# This is a permuttation function using rescursion factorial.
def combination(n,r):
    comb = permutation(n,r)/factorial(r)
    return int(comb)
value_of_n = int(input("Enter the value of number(n): "))
value_of_r = int(input("Enter the value of common ratio(r): "))
print(f"The value of permutation is: {permutation(value_of_n,value_of_r)}")
print(f"The value of combination is: {combination(value_of_n,value_of_r)}")





