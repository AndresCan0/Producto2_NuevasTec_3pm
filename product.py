from db_connection import DBConnection

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name 
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_products_by_price(self, min_price, max_price):
        sql = f"SELECT * FROM products WHERE price BETWEEN {min_price} AND {max_price}"
        result = db.query(sql)
        return result