class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, 'Kat')
setattr(student, 'student_email', 'test@test.com')
print(f'Student Name:', getattr(student, 'name'), '\nStudent Email:', getattr(student, 'student_email'))