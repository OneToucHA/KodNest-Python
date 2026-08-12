
class StudentProfile:
    def __init__(self, student_id, name, course, score, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        placement_str = "Placed" if self.is_placed else "Not Placed"
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {placement_str}"
        )


# Read inputs
student_id = int(input().strip())
name = input().strip()
course = input().strip()
score = float(input().strip())
placement_input = input().strip()

# Convert placement input to Boolean
is_placed = placement_input.lower() == "yes"

# Create object using keyword arguments
student = StudentProfile(
    student_id=student_id,
    name=name,
    course=course,
    score=score,
    is_placed=is_placed
)

# Print the profile
print(student)