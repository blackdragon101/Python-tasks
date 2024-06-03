def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            print(f"Element found at index {i}")
            return i
    print("Element not found")
    return -1
search_element = int(input("Enter the number you want to search in the given data list: "))
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return list3

search_list_string = input("Enter the list in which you want to search: ")
search_list=type_conversion_from_string_to_list(search_list_string)
answer = linear_search(search_list,search_element)
print(answer)
