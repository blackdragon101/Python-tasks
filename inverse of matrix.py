matrix1 = list(input("Enter the first nested list: "))
matrix2 = list(input("Enter the second nested list: "))
main_matrix = [matrix1,matrix2]
a,b = matrix1[0],matrix1[1]
c,d = matrix2[1],matrix2[1]
A = int(a)
B = int(b)
C = int(c)
D = int(d)

determinant = A*D - B*C
try:
    if determinant ==0:
        raise Exception("The matrix is non convertible.")
except:
    matrix1 = list(input("Enter the first nested list: "))
    matrix2 = list(input("Enter the second nested list: "))


adj = [[D,-B],[-C,A]]
inverse = [[elements/determinant for elements in row] for row in adj]
for rows in inverse:
    print(rows)



