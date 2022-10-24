class School:
    def __init__(self, name, address, principal='') -> None:
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)


class Grade:
    def __init__(self, name, teacher) -> None:
        self.students = []
        self.name = name
        self.teachers = teacher

    def __repr__(self) -> str:
        return f"'{self.name}', '{self.teachers}'"


oxford = School("Oxford kid Academy", "Mirpur", "Obayed Alam")
oxford.add_grade("Class 3", "Osman Gani")
oxford.add_grade("Class 1", "Nahim Bulhan")

print(oxford.grades)
