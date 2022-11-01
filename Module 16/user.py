import hashlib


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open("users.txt", "w") as file:
            file.write(
                f"{email} {pwd_encrypted}")
        file.close()
        print(self.name, "User created")

    @staticmethod
    def login(email, password):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_pwd = line.split(" ")[1]
        file.close()

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if (hashed_password == stored_pwd):
            print("Successfully logged in")
            return True
        else:
            print("goaway hacked lol")
            return False


def Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super.__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


def Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super.__init__(name, email, password)
        self.location = location
        self.license = license
        self.salary = 0

    def start_a_trip(self, destination, fare):
        self.salary += fare
        self.location = destination


Hero = User("Hero alom", "hero@alim.com", "heroOhHero")
Hero.login("hero@alim.com", "heroOhHero")
