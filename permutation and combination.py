def factorial(no):
    """This is a udf that provides us with the factorial of a number."""
    fact = 1
    while no>1:
        fact = fact * no
        no -= 1
    return(fact)
def permute(n1,r1):
    """This is a udf that provides us with the permutation of given numbers n and r."""
    perm = factorial(n1) / factorial(n1-r1)
    return int(perm)
def combine(n2,r2):
    """This is a udf that provides us with the combination of given numbers n and r."""
    combination = permute(n2,r2)/factorial(r2)
    return int(combination)

perm_or_comb = input("""Enter 1 or 2:
1.Permutation
2.Combination """)
if perm_or_comb == '1':
    n1 = int(input("""Enter the value of n 
 (The value of n must be greater then r) """))
    r1 = int(input("Enter the value of r "))
    print(f"The permutation is: {permute(n1,r1)}")
if perm_or_comb == '2':
    n2 = int(input("Enter the value of n.(The value of n > r) "))
    r2 = int(input("Enter the value of r "))
    print(f"The combination is: {combine(n2,r2)}")








