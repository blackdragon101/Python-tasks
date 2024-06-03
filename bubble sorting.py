def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        print(f"Iteration {i+1}: {arr}")
    print("Total swaps:", swaps)
    return arr
def type_conversion_from_string_to_list(string):
    list1 = string.replace('[','')
    list2 = list1.replace(']','')
    list3 = list2.split(',')
    return list3
input_list = input("Enter a list you want to sort: ")
To_sort_list = type_conversion_from_string_to_list(input_list)
sorted = bubble_sort(To_sort_list)
print(sorted)

