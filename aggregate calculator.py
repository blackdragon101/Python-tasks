# This is a python program to calculate the aggregate of a student.
ecat_marks = int(input("Enter your ECAT marks "))
inter = int(input("Enter your obtained inter part 1 marks  "))
total_inter = int(input("Enter the total marks of fsc first year "))
matric = int(input("Enter your matriculation marks "))
percent_ecat = (ecat_marks/400) * 33
percent_mat = (matric/1100) * 17
percent_int = (inter/total_inter) * 50
aggregate = percent_int + percent_ecat + percent_mat
result = round(aggregate,2)
print(f"Your aggregate is:{result}")




