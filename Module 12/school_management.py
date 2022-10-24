class School:
    def __init__(self, name, address, principal='') -> None:
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade(self, name):
        idx = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
                idx = i

        del self.grades[idx]


class Grade:
    def __init__(self, name, teacher) -> None:
        self.students = []
        self.name = name
        self.teachers = teacher

    def __repr__(self) -> str:
        return f"'{self.name}', '{self.teachers}'"

    def __del__(self) -> None:
        print(f"Deleting {self.name} with teacher {self.teachers}")


oxford = School("Oxford kid Academy", "Mirpur", "Obayed Alam")
oxford.add_grade("Class 1", "Nahim Bulhan")
oxford.add_grade("Class 3", "Osman Gani")
oxford.add_grade("Class 5", "Bulhan Udin")

oxford.remove_grade("Class 5")

print(oxford.grades)
