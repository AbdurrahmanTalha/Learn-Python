class Phone:
    manufactured = "America"

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self, number, text):
        sms = f" sending: {text} to {number}"
        return sms


my_phone = Phone("Apple", 1200, "black")
print(my_phone.brand, my_phone.manufactured)

her_phone = Phone("Oppo", 800, "purple")
print(her_phone.brand, her_phone.manufactured)

dad_phone = Phone("Nokia", 700, "black")
print(my_phone.price, her_phone.price, dad_phone.price)
