# Exercise: Create a Class for Inventory Management

# Create a class called Inventory.
# The class should have the following attributes:
# products (a dictionary to store the products in the inventory with their product IDs as keys and product instances as values).
# The class should have the following methods:
# add_product(product): Adds a product to the inventory.
# remove_product(product_id): Removes a product from the inventory based on its product ID.
# get_product(product_id): Returns the product instance from the inventory based on its product ID.
# display_inventory(): Displays the list of products and their details in the inventory.
# Create another class called Product (similar to the previous exercise).
# Test your classes by creating instances of Product and Inventory, adding products to the inventory, removing products, and displaying the inventory details.
# Example Usage:

# python
# Copy code
# # Create product instances
# product1 = Product(1, 'T-Shirt', 15.99, 50)
# product2 = Product(2, 'Jeans', 29.99, 30)

# # Create an inventory instance
# inventory = Inventory()

# # Add products to the inventory
# inventory.add_product(product1)
# inventory.add_product(product2)

# # Display the inventory details
# inventory.display_inventory()

# # Get a product by its ID
# product_id = 1
# product = inventory.get_product(product_id)
# if product:
#     print(f"Product ID: {product_id}")
#     product.display_product_info()

# # Remove a product by its ID
# product_id_to_remove = 2
# inventory.remove_product(product_id_to_remove)

# # Display the updated inventory details
# inventory.display_inventory()
# Expected Output:

# yaml
# Copy code
# Inventory Details:
# Product ID: 1
# Product Name: T-Shirt
# Price: $15.99
# Quantity: 50
# Product ID: 2
# Product Name: Jeans
# Price: $29.99
# Quantity: 30
# Product ID: 1
# Product Name: T-Shirt
# Price: $15.99
# Quantity: 50
# In this exercise, we have two classes: Product for modeling individual products, and Inventory for managing the collection of products. The Inventory class uses a dictionary to store the products with their unique product IDs as keys.

# Feel free to customize the classes and add more functionalities if you wish to extend the inventory management system. For example, you could add methods to update product details (price, quantity) or handle out-of-stock scenarios. Happy coding and practicing!


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self, quantity):
        return self.price * quantity

    def update_quantity(self, sold_quantity):
        if sold_quantity <= self.quantity:
            self.quantity -= sold_quantity
        else:
            print("Insufficient quantity. Sale canceled.")

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found in the inventory.")

    def get_product(self, product_id):
        return self.products.get(product_id)

    def display_inventory(self):
        print("Inventory Details:")
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}")
            product.display_product_info()


# Example Usage
product1 = Product(1, 'T-Shirt', 15.99, 50)
product2 = Product(2, 'Jeans', 29.99, 30)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

inventory.display_inventory()

# product_id = 1
# product = inventory.get_product(product_id)
# if product:
#     print(f"Product ID: {product_id}")
#     product.display_product_info()

# product_id_to_remove = 2
# inventory.remove_product(product_id_to_remove)

# inventory.display_inventory()
