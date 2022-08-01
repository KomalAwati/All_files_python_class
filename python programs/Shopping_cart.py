class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity, price):
        self.cart.append({ "name": name, "quantity": quantity, "price":  price})

c1 = ShoppingCart()
c1.add_item("Komal", 2 , 2000)
