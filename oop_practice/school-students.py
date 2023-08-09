class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        student.set_school(self)

    def __str__(self):
        return f"School: {self.name} located in {self.location}"

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.school = None

    def set_school(self, school):
        self.school = school

    def enrolled_school(self):
        if self.school:
            return f"Enrolled in: {self.school.name} located in {self.school.location}"
        else:
            return "Not enrolled in any school."

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

# Create school instances
school1 = School("ABC High School", "Cityville")
school2 = School("XYZ Academy", "Townsville")

# Create student instances
student1 = Student("Alice", 16)
student2 = Student("Bob", 17)
student3 = Student("Eve", 15)

# Enroll students in schools
school1.enroll_student(student1)
school1.enroll_student(student2)
school2.enroll_student(student3)

# Print school information along with enrolled students
for school in [school1, school2]:
    print(school)
    if school.students:
        print("Enrolled Students:")
        for student in school.students:
            print(student)
        print()
    else:
        print("No students enrolled\n")

# Display students' enrolled schools
for student in [student1, student2, student3]:
    print(student)
    print(student.enrolled_school())
    print()
