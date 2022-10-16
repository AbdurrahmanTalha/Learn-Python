class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10_000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return "You are withdrawing to little"
        elif amount > self.max_withdraw:
            return "Don't be so greedy"
        elif amount > self.balance:
            return "You don't have enough money"
        else:
            self.balance -= amount
            return f"Here is ur money"

    def deposit(self, amount):
        self.balance += amount
        return "Added ur money"


my_bank = Bank(8000)
reply = my_bank.deposit(10000)
print(reply)
