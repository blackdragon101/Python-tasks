search_word = input("Enter the string which you want to search: ")
file_inp = input("Enter the file name in which you want to search: ")
file = open(file_inp,'r')
lines = file.readlines()
print(lines)
for line in lines:
    list = line.split()
    if search_word in list:
        print("The search word is found in this file")
        print(f"The line number is: {lines.index(line)+1}")
        break
    else:
        print("The search word is not found in file.")
        break
file.close()





