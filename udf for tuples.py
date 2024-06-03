def from_string_to_tuple(string):
    str1 = string.replace('(','')
    str2 = str1.replace(')','')
    str3 = str2.split(',')
    final = tuple(str3)
    return final
input1 = input("Enter the 1st tuple: ")
tuple1 = from_string_to_tuple(input1)
input2 = input("Enter the 2nd tuple:")
tuple2 = from_string_to_tuple(input2)
list1 = []
for elements in range(0,len(tuple1)):
    for values in range(0,len(tuple2)):
        if tuple1[elements] == tuple2[values]:
            list1.append(tuple1[elements])
result = tuple(list1)
print(result)







