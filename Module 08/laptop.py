class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self, age=1):
        self.last_age = self.age
        self.age = self.age+age

    def repair(self, lifeIncrease):
        self.increase_age(-5)


my_laptop = Laptop("Apple", 0.3)
my_laptop.increase_age()
my_laptop.age = 17
my_laptop.repair(10)
my_laptop.increase_age()
print(my_laptop.age)
