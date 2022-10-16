class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class School:
    def __init__(self, name, teacher, courses, students):
        self.name = name
        self.teachers = teacher
        self.courses = courses
        self.students = students

    def get_students(self):
        for students in self.students:
            print(students.name);

school_name = "Phitron"

ds_course = Course("Data Structure", "Einstein")
teacher_1 = Teacher("Einstein", ds_course)

algo_course = Course("Algorithm", "Edison")
teacher_2 = Teacher("Edison", algo_course)

student_1 = Student("Rhomot", 19, 45)
student_2 = Student("Anar Ali", 17, 96)
student_3 = Student("Alia Bhatt", 29, 72)

teachers = [teacher_1, teacher_1]
courses = [ds_course, algo_course]
students = [student_1, student_2, student_3]

my_school = School(school_name, teachers, courses, students)

my_school.get_students()
