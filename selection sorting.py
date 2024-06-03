def selection_sort(argument):
    n = len(argument)
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if argument[j] < argument[min_index]:
                min_index = j
        argument[i], argument[min_index] = argument[min_index], argument[i]
        swaps += 1
        print(f"Iteration {i+1}: {argument}")
    print("Total swaps:", swaps)
    return argument
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return list3
to_sort_list = input("Enter the list to be sorted: ")
new_list = type_conversion_from_string_to_list(to_sort_list)
sorted_list = selection_sort(new_list)
print(sorted_list)
