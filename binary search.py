def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return list3
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    searches = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            print(f"Element found at index {mid}")
            print("Total searches:", searches)
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        searches += 1
    print("Element not found")
    print("Total searches:", searches)
    return -1
search_num = int(input("Enter the number you want to search: "))
search_list_string = input("Enter the list in which you want to search: ")
search_list = type_conversion_from_string_to_list(search_list_string)
a = binary_search(search_list,search_num)
print(a)
