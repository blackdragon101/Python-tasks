def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return(list3)
list = input("Enter the list: ")
input_list = type_conversion_from_string_to_list(list)
input_list.sort()
iterations = len(input_list)
for index in range(0,iterations):
    if index == len(input_list)-1:
        break
    for i in range(1,iterations):
        if index == i:
            i = i + 1
        if i == iterations:
            break
        if input_list[index] == input_list[i]:
            input_list.pop(index)
            iterations = iterations - 1
output_list = input_list.copy()
print(output_list)
















