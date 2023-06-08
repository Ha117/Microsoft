class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, gender, grade):
        s = Student(name, age, gender, grade)
        self.students.append(s)

    def remove_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)

    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def print_students(self):
        for s in self.students:
            print('Name:', s.name)
            print('Age:', s.age)
            print('Gender:', s.gender)
            print('Grade:', s.grade)
            print('')

# 示例代码
sys = StudentSystem()
sys.add_student('Tom', 18, 'Male', 'Grade 1')
sys.add_student('Lucy', 17, 'Female', 'Grade 2')
sys.add_student('John', 19, 'Male', 'Grade 3')
sys.print_students()
sys.remove_student('Lucy')
s = sys.find_student('Tom')
if s:
    print('Find student:', s.name)
else:
    print('Cannot find student')
