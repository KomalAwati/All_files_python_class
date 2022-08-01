#Pgm-1
#ShoppingCart add_item
'''
class ShoppingCart:
    # class Variable
    prices = { "iPhone": 800, "iMac": 2500, "iWatch": 3000, "iPad": 3500 }
    products = { "iPhone": 5, "iMac": 3, "iWatch": 2, "iPad": 4 }
    
    def __init__(self):
        self.cart = [ ]

    def add_item(self, name, quantity):
        if name not in ShoppingCart.products:
            raise Exception("Product not available")
        elif quantity > ShoppingCart.products[name]:
            raise Exception("Product out of stock")
        else:
            self.cart.append({ "name": name, "quantity": quantity, "price":  ShoppingCart.prices[name]})
            ShoppingCart.products[name] -= quantity #ShoppingCart.products[name] = ShoppingCart.products[name] - quantity

            
c1 = ShoppingCart()
c2 = ShoppingCart()

c1.add_item('iPhone',3)
print(c1.__dict__)

c2.add_item('iPhone',3)
print(c2.__dict__)
'''
#O/p-
#{'cart': [{'name': 'iPhone', 'quantity': 3, 'price': 800}]}
#Exception: Product out of stock


#*****************************************************************************************************************************#Pgm-1
#Pgm-2
#ShoppingCart add_item and remove_item
class ShoppingCart:
    # class Variable
    prices = { "iPhone": 800, "iMac": 2500, "iWatch": 3000, "iPad": 3500 }
    products = { "iPhone": 5, "iMac": 3, "iWatch": 2, "iPad": 4 }

    def __init__(self):
        self.cart = [ ] #c1.cart or c2.cart
    
    def add_item(self, name, quantity):
        if name not in ShoppingCart.products:
            raise Exception("Product not available")
        elif quantity > ShoppingCart.products[name]:
            raise Exception("Product out of stock")
        else:
            self.cart.append({ "name": name, "quantity": quantity, "price":  ShoppingCart.prices[name]})
            ShoppingCart.products[name] -= quantity

    def remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] > 1:
                    item['quantity'] = item['quantity'] - 1
                else:
                    self.cart.remove(item)

    def total_cost(self):
        total = 0.00
        for item in self.cart:
            total += item['quantity'] * item['price']
        return total

c1 = ShoppingCart()
c2 = ShoppingCart()

##
#O/p
'''
c1.cart
[]


c2.cart
[]


c1.add_item('iPhone',2)
c1.__dict__
{'cart': [{'name': 'iPhone', 'quantity': 2, 'price': 800}]}


c2.add_item('iPhone',1)
c2.__dict__
{'cart': [{'name': 'iPhone', 'quantity': 1, 'price': 800}]}

ShoppingCart.products
{'iPhone': 2, 'iMac': 3, 'iWatch': 2, 'iPad': 4}

c1.remove_item('iPhone')
c1.__dict__
{'cart': [{'name': 'iPhone', 'quantity': 1, 'price': 800}]}

for item in c1.cart:
    print(item)
{'name': 'iPhone', 'quantity': 1, 'price': 800}

c1.add_item('iMac',2)
c1.__dict__
{'cart': [{'name': 'iPhone', 'quantity': 1, 'price': 800}, {'name': 'iMac', 'quantity': 2, 'price': 2500}]}

c1.total_cost()
5800.0
'''
##
'''
c1.cart
[{'name': 'iPhone', 'quantity': 1, 'price': 800}]
c2.cart
[{'name': 'iPhone', 'quantity': 1, 'price': 800}]

ShoppingCart.products
{'iPhone': 2, 'iMac': 3, 'iWatch': 2, 'iPad': 4}
'''



