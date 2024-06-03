list_by_user = input("Enter the list: ")
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return(list3)
new_list = type_conversion_from_string_to_list(list_by_user)
new_list.sort()
iterations = len(new_list)
for index in range(0,iterations):
    if index == len(new_list)-1:
        break
    for i in range(1,iterations):
        if index == i:
            i = i + 1
        if i == iterations:
            break
        if new_list[index] == new_list[i]:
            new_list.pop(index)
            iterations = iterations - 1
output_list = new_list.copy()
print(f"The second smallest number in the list:{output_list[1]}")



