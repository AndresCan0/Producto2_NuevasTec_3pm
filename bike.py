from product import Product

class Bike(Product):

    def __init__(self, id, name, price, size, type):
        super().__init__(id, name, price)
        self.size = size
        self.type = type

    def display_bike_info(self):
        print(f"Bike Name: {self.name}")
        print(f"Bike Price: {self.get_price()}")
        print(f"Bike Size: {self.size}")
        print(f"Bike Type: {self.type}")