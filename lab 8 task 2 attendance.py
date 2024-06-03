total_classes = int(input("Enter the total number of classes of PF course: "))
atten_file = open('attendance file','w')
for classes in range(total_classes):
    pres_student = int(input(f"Enter the total no of students present in class{classes+1}: "))
    for i in range(pres_student):
        name = input(f"Enter the name of student {i+1}: ")
        atten_file.write(name)
        atten_file.write('\n')
atten_file.close()
file1 = open('attendance file','r')
names_list = file1.readlines()
atten_dict = {}
for names in names_list:
    count = names_list.count(names)
    atten_dict[names] = count
file1.close()
def percent_atten(student,count):
    percent = int((count/total_classes) * 100)
    print(f"The attendance percentage of {student} is: {percent}")
    if percent < 40:
        print('Not Eligible to sit in exam.')
    else:
        print("Eligible to sit in the exam.")
    return
for keys,values in atten_dict.items():
    percent_atten(keys,values)







