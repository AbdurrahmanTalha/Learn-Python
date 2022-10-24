# laptop, phone, tablet, computer, watch

class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def purchase(self, money):
        if (money < self.price):
            return "Pay more money"
        else:
            print("Here is ur laptop")
            return money - self.price


class Laptop(Device):

    def __init__(self, brand, price, color, disc_size) -> None:
        super().__init__(brand, price, color)
        self.disc_size = disc_size

    def run(self):
        print("Running the laptop")

    def __repr__(self) -> str:
        return f"Laptop {self.brand}: {self.price} : {self.color} : {self.disc_size}"


class Phone:
    def __init__(self, brand, price, color, camera, sim_num) -> None:
        super().__init__(brand, price, color)
        self.camera = camera
        self.sim_num = sim_num

    def is_dual_sim(self) -> None:
        return self.sim_num > 1


class Watch:
    def __init__(self, brand, price, color, watch_type) -> None:
        super().__init__(brand, price, color)
        self.watch_type = watch_type

    def is_digital(self) -> None:
        return self.watch_type == "digital"


class Manager:
    def __init__(self, name, salary, experience, designation) -> None:
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complaint(self):
        pass


class SalesPerson:
    def __init__(self, name, salary, experience, designation, commission) -> None:
        pass

    def handle_customer(self):
        pass


lenova = Laptop("Lenova", 42000, "black", "1tb")
print(lenova)
