input1 = input("Enter the values of first row: ")
input2 = input("enter the values of second row: ")
input3 = input("Enter the values of third row: ")
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return(list3)
row1 = type_conversion_from_string_to_list(input1)
row2 = type_conversion_from_string_to_list(input2)
row3 = type_conversion_from_string_to_list(input3)
matrix = [row1,row2,row3]
transpose = []
for j in range(len(matrix[0])):
    r1 = []
    for i in range(len(matrix)):
        r1.append(matrix[i][j])
    transpose.append(r1)
print(f"The matrix is:{matrix}")
print(f"The transpose of the following matrix is:{transpose}")























