class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []  # Initialize an empty list to hold related students

    def add_student(self, student):
        self.students.append(student)
        student.set_teacher(self)  # Set the student's teacher reference

class Student:
    def __init__(self, name):
        self.name = name
        self.teacher = None  # Initialize the teacher reference as None

    def set_teacher(self, teacher):
        self.teacher = teacher

# Create instances of Teacher and Student
teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Ms. Johnson")
teacher3= Teacher("Mr Justin")

student1 = Student("Alice")
student2 = Student("Bob")
student3= Student("Jaden")

# Associate students with teachers
teacher1.add_student(student1)
teacher2.add_student(student2)
teacher2.add_student(student3)

# Print teacher and student information
for teacher in [teacher1, teacher2, teacher3]:
    print(f"Teacher: {teacher.name}")
    if teacher.students:
        print("Students:")
        for student in teacher.students:
            print(f"- {student.name}")
    else:
        print("No students assigned\n")

    print()
