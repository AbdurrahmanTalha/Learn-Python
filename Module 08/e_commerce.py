class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'name': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        price = 0
        for i in self.cart:
            price += i['price'] * i['quantity']

        if (amount < price):
            return f"please give me more money: {price-amount}"
        elif (amount > price):
            return f"Here is the remaining money: {amount-price}"
        elif(amount == price):
            return f"Thank you for buying here"

shopping = Shopper('Bag Tan')
shopping.add_to_cart("shirt", 400, 3)
shopping.add_to_cart("shoes", 899, 4)
shopping.add_to_cart("pant", 1400, 2)

reply = shopping.checkout(7596)
print(reply)
