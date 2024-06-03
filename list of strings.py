variable_list = [7,'fatima',9,[1,'family',3],{'iknow',4,6},('finland',56),'dog']
def is_string(in_list):
    string_list = []
    for elements in in_list:
        if isinstance(elements,str):
            string_list.append(elements)
        elif isinstance(elements,(tuple,set,list)):
            string_list.extend(is_string(elements))
    return string_list
print(is_string(variable_list))


