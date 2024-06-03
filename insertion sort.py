def insertion_sort(parameter):
    n = len(parameter)
    swaps = 0
    for i in range(1, n):
        key = parameter[i]
        j = i - 1
        while j >= 0 and key < parameter[j]:
            parameter[j + 1] = parameter[j]
            j -= 1
            swaps += 1
        parameter[j + 1] = key
        print(f"Iteration {i}: {parameter}")
    print("Total swaps:", swaps)
    return parameter
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return list3
to_sort_list = input("Enter the list to be sorted: ")
new_list = type_conversion_from_string_to_list(to_sort_list)
sorted_list = insertion_sort(new_list)
print(sorted_list)
