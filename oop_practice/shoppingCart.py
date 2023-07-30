
# Exercise: Create a Class for an Online Shopping System

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
# Create another class called ShoppingCart.
# The class should have the following attributes:
# items (a dictionary to store the products added to the shopping cart and their quantities).
# The class should have the following methods:
# add_to_cart(product, quantity): Adds a product and its quantity to the shopping cart.
# remove_from_cart(product): Removes a product from the shopping cart.
# calculate_total_price(): Calculates and returns the total price of all products in the shopping cart.
# display_cart_items(): Displays the items in the shopping cart along with their quantities.
# Test your classes by creating instances of Product and ShoppingCart, and performing some shopping cart operations.
# Example Usage:

# python
# Copy code
# # Create product instances
# product1 = Product(1, 'T-Shirt', 15.99, 50)
# product2 = Product(2, 'Jeans', 29.99, 30)

# # Create a shopping cart instance
# cart = ShoppingCart()

# # Add products to the cart
# cart.add_to_cart(product1, 2)
# cart.add_to_cart(product2, 1)

# # Display the cart items
# cart.display_cart_items()

# # Calculate and display the total price
# total_price = cart.calculate_total_price()
# print(f"Total price: ${total_price:.2f}")
# Expected Output:

# yaml
# Copy code
# Shopping Cart Items:
# T-Shirt (Product ID: 1) - Quantity: 2
# Jeans (Product ID: 2) - Quantity: 1
# Total price: $61.97
# Feel free to try this exercise and expand on the classes if you'd like to add more functionalities, such as updating product details, handling out-of-stock scenarios, or adding discounts to the products. This exercise will provide you with a practical example of modeling an online shopping system using Python classes and objects. Happy coding and practicing!


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


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_from_cart(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print("Product not found in the cart.")

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.get_total_price(quantity)
        return total_price

    def display_cart_items(self):
        print("Shopping Cart Items:")
        for product, quantity in self.items.items():
            print(f"{product.name} (Product ID: {product.product_id}) - Quantity: {quantity}")


# Example Usage
product1 = Product(1, 'T-Shirt', 15.99, 50)
product2 = Product(2, 'Jeans', 29.99, 30)

cart = ShoppingCart()
cart.add_to_cart(product1, 2)
cart.add_to_cart(product2, 6)

cart.display_cart_items()

total_price = cart.calculate_total_price()
print(f"Total price: ${total_price:.2f}")