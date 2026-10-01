def student_details(name, roll_no):
    print("\n----- Student Details -----")
    print("Student Name:", name)
    print("Roll Number:", roll_no)


def calculate_total(a1, a2, a3):
    total = a1 + a2 + a3
    return total


def calculate_average(total):
    average = total / 3
    return average


def get_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


def show_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

student_details(name, roll_no)

print("\nEnter marks for three subjects:")

a1 = int(input("Subject 1: "))
a2 = int(input("Subject 2: "))
a3 = int(input("Subject 3: "))

total = calculate_total(a1, a2, a3)

average = calculate_average(total)

result = get_result(average)

grade = show_grade(average)

print("\n----- Student Result -----")
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)
print("Grade:", grade)