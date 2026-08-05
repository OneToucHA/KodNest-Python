#Read marks , attendence and project completion status
Marks=int(input("Enter the Student marks: "))
Attendence=int(input("Enter the Student attendence: "))
project_completion=input("Enter the Student project completion status(yes/no): ")
if Marks>60 and Attendence>75:
    if project_completion =="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
        