# Exercise: Create Classes for Order Management

# Create a class called Product.

# The class should have the following attributes:

# product_id (a unique identifier for each product).
# name (the name of the product).
# price (the price of the product).
# quantity (the available quantity of the product).
# The class should have the following methods:

# get_total_price(quantity): Calculates and returns the total price for a given quantity of the product.
# update_quantity(sold_quantity): Updates the quantity of the product after it's been sold.
# display_product_info(): Displays information about the product (product_id, name, price, and quantity).
# Create a class called Order.

# The class should have the following attributes:

# customer_name (the name of the customer placing the order).
# items (a dictionary to store the products in the order with their product instances as keys and their quantities as values).
# The class should have the following methods:

# add_item(product, quantity): Adds a product and its quantity to the order.
# remove_item(product): Removes a product from the order.
# calculate_total(): Calculates and returns the total price of the order.
# display_order(): Displays the items in the order along with their quantities and the total price.
# Test your classes by creating instances of Product and Order, adding products to the order, removing products, and displaying the order details.

# Example Usage:

# python
# Copy code
# # Create product instances
# product1 = Product(1, 'T-Shirt', 15.99, 50)
# product2 = Product(2, 'Jeans', 29.99, 30)

# # Create an order instance
# order = Order('John Doe')

# # Add products to the order
# order.add_item(product1, 2)
# order.add_item(product2, 1)

# # Display the order details
# order.display_order()
# Expected Output:

# mathematica
# Copy code
# Order Details for John Doe:
# Product ID: 1, Product Name: T-Shirt, Quantity: 2
# Product ID: 2, Product Name: Jeans, Quantity: 1
# Total Price: $61.97
# In this exercise, we have two classes: Product for modeling individual products, and Order for managing a customer's order. The Order class uses a dictionary to store the products in the order with their respective quantities.

# Feel free to customize the classes and add more functionalities if you wish to extend the order management system. For example, you could add methods to update quantities in the order, handle out-of-stock scenarios, or provide a summary of the order with additional information such as shipping address and order date. Happy coding and practicing!

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


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print("Product not found in the order.")

    def calculate_total(self):
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.get_total_price(quantity)
        return total_price

    def display_order(self):
        print(f"Order Details for {self.customer_name}:")
        for product, quantity in self.items.items():
            print(f"Product ID: {product.product_id}, Product Name: {product.name}, Quantity: {quantity}")
        total_price = self.calculate_total()
        print(f"Total Price: ${total_price:.2f}")


# Example Usage
product1 = Product(1, 'T-Shirt', 15.99, 50)
product2 = Product(2, 'Jeans', 29.99, 30)

order = Order('John Doe')
order.add_item(product1, 2)
order.add_item(product2, 1)

order.display_order()
