from user import User 
from bike import Bike
from db_connection import DBConnection

# Crear objetos 
user1 = User(1, 'john', 'password123')
bike1 = Bike(1, 'Mountain Bike', 200, 'M', 'Mountain')

# Conexion al base de datos
db = DBConnection()

# Login 
user1.login()

# Mostrar la info de la bici
bike1.display_bike_info()

# Query de productos por rango de precio  
min_price = 100
max_price = 500
results = bike1.get_products_by_price(min_price, max_price)

# Cerrar base de datos
db.close()