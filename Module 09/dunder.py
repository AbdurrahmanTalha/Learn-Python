class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def __add__(self, other):
        return self.age + other.age

    def __call__(self):
        return f"This is {self.name} with age {self.age} and have {self.money}"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        rep = "Name(" + self.name + ")"
        return rep


alim = Person("Alim", 16, 400)
dalim = Person("Dalim", 16, 500)

# print(alim + dalim)

x = 5
# print(type(alim))
print(repr(alim))
