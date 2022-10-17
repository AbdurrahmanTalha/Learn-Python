class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f'{self.f_name}.{self.l_name}@user.com'

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    @full_name.setter
    def full_name(self, value):
        self.f_name = value.split(" ")[0]
        self.l_name = value.split(" ")[1]

    @full_name.deleter
    def full_name(self):
        del self.f_name
        del self.l_name

    def get_email(self):
        return self.email


mark = User("Mark", "zuku")
print(mark.f_name)
print(mark.l_name)
print(mark.email)
print(mark.get_email())
print(mark.full_name)
mark.full_name = "Tom Hanks"
print(mark.full_name)
print(mark.email)
del mark.full_name

