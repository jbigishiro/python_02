class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.store = None

    def set_store(self, store):
        self.store = store

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}"

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        product.set_store(self)

    def display_products(self):
        if self.products:
            print(f"Products available at {self.name}:")
            for product in self.products:
                print(product)
            print()
        else:
            print(f"No products available at {self.name}\n")

    def __str__(self):
        return f"Store: {self.name} located in {self.location}"

# Create store instances
store1 = Store("Electronics World", "City Center")
store2 = Store("Fashion Haven", "Mall Street")

# Create product instances
product1 = Product("Laptop", 999.99)
product2 = Product("Smartphone", 599.99)
product3 = Product("Dress Shirt", 49.99)

# Associate products with stores
store1.add_product(product1)
store1.add_product(product2)
store2.add_product(product3)

# Print store information along with products
for store in [store1, store2]:
    print(store)
    store.display_products()

# Display store's products
for product in [product1, product2, product3]:
    print(product)
    if product.store:
        print(f"Available at: {product.store.name}")
    else:
        print("Not available at any store")
    print()
