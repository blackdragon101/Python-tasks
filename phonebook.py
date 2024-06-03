phonebook = {'rafia':3137452,'khush':3009876,'Ali':3137890,'Ammar':3336578,'mishal':3225674}
def search_by_name(x):
    if x in phonebook:
        print(phonebook[x])
    else:
        print("The contact does not exist in your phonebook.")
    return
def names_of_all_contacts():
    print(phonebook.keys())
    return
def contact_no_display():
    print(phonebook.values())
def delete_number(y):
    if y in phonebook:
        phonebook.pop(y)
        print(phonebook)
    else:
        print("This contact already does not exist.")
    return
def delete_whole_phonebook():
    phonebook.clear()
    print(phonebook)
    return
def phonebook_update(name,contact):
    phonebook.update({name:contact})
    print(phonebook)
    return
delete_number('Ammar')
phonebook_update('fatima',3134567)
search_by_name('rafia')
contact_no_display()
names_of_all_contacts()








