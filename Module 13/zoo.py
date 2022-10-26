from abc import ABC, abstractmethod


# Abstract class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    def move(self):
        pass


class Money(Animal):
    def eat(self):
        print("**eating** banana")

    def sing(self):
        print("KAWK KAKW AKKAK AKKWAW")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


layka = Money()
layka.name = "MONKEYYEYE"
print(layka.name)
