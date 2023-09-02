# Nested Methods Example

# This code demonstrates the concept of nested methods in Python.
# A nested method is a method that is defined inside another method.
# Bakery Example with Nested Methods

class Bakery:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        def bake():
            print(f"{product_name} is being baked at {self.name}")

        self.products.append(product_name)
        bake()

    def list_products(self):
        print(f"{self.name} offers the following products:")
        for product in self.products:
            print("- " + product)

# Inside the 'add_product' method, we have a nested method called 'bake' that simulates the baking process.
# When a product is added to the bakery, the 'bake' method is called to indicate that the product is being baked.

# Creating bakery instances
bakery1 = Bakery("Sweet Delights")
bakery2 = Bakery("Flour Magic")

# Adding products
bakery1.add_product("Croissant")
bakery1.add_product("Chocolate Cake")

bakery2.add_product("Baguette")
bakery2.add_product("Blueberry Muffin")

# Listing products
bakery1.list_products()
bakery2.list_products()
