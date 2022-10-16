
class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


shopper_1 = Shop("Talha")
shopper_1.add_to_cart("food")
print(shopper_1.cart)

shopper_2 = Shop("Shakib")
shopper_2.add_to_cart("shoes")
print(shopper_2.cart)
