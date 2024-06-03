def gpa_cal():
    """This is a UDF to calculate the gpa of a semester."""
    total_subs = int(input("Enter the total subjects you have studied in this semester: "))
    sum_of_total_gp = 0
    sum_of_credits = 0
    for names in range(1,total_subs+1) :
        gp = float(input(f"Enter the grade points you got in {names} subject: "))
        credit_hrs = int(input("Enter the credit hours for this course: "))
        sum_of_credits = sum_of_credits + credit_hrs
        total_gp = gp*credit_hrs
        sum_of_total_gp = sum_of_total_gp + total_gp
    cgpa = round(sum_of_total_gp/sum_of_credits,2)
    # This round method is used to round off the answer to specified decimal places.
    return cgpa
print(gpa_cal())







