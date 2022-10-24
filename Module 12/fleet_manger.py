class Bus:
    owner = "brad"

    def __init__(self, route, license, driver):
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []

    def start_trip(self, start_time):
        self.trips.append(start_time)


class Driver:
    def __init__(self, name, address, salary, license):
        self.name = name
        self.address = address
        self.salary = salary
        self.license = license

    def drive(self, start, end):
        pass

    def withdraw_salary(self):
        pass


class Passenger:
    def __init__(self, name, mobile, destination) -> None:
        self.name = name
        self.mobile = mobile
        self.destination = destination

    def purchase_ticket(self, destination, money) -> None:
        pass


class Manager:
    def __init__(self, name, mobile, department) -> None:
        pass


class Counter:
    def __init__(self, manager, location) -> None:
        pass


num = 55
name = "Anna"
rashed = Passenger("Rashed", "01777", "Khulna")
