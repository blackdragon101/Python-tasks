import random
ran_list = []
for i in range(10):
    random_num = random.randint(0, 1000)
    ran_list.append(random_num)
print(f"The list of generated numbers is: {ran_list}")
def sum_list_recursive(numbers, index):
    if index == len(numbers):
        return 0
    else:
        return numbers[index] + sum_list_recursive(numbers, index + 1)
resulting_sum = sum_list_recursive(ran_list,0)
print(f"The resulting sum is :{resulting_sum}")



