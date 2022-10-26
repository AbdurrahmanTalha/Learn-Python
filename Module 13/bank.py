class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

   

class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school):
        self.school = school
        super().__init__(holder, initial_balance)
    def getBalance(self):
        return self.__balance


rafsan = StudentAccount("Rafsan", 50_000, "J.C.P.S.C")

rafsan.deposit(20_000)
rafsan.deposit(35_000)
rafsan.deposit(15_000)

print(rafsan.getBalance())
