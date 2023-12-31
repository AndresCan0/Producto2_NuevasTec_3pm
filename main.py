# main.py
import sqlite3, os
from users.worker import Admin
from users.work import Work
from database.connection import DataBase

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():
    db = DataBase()
    db.connect()
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("\n<- Elija una opción: ")
        if opcion == "1":
            limpiar_consola()
            register_user(db)
        elif opcion == "2":
            limpiar_consola()
            login_user(db)
        elif opcion == "3":
            limpiar_consola()
            db.close()
            break
        else:
            limpiar_consola()
            print("\n -> Opción no válida. Intente de nuevo.")
def register_user(db):
    print("\n -> Opcion de registrarse.")
    username = input("\n<- Usuario: ")
    password = input("<- Contraseña: ")
    user_type = input("<- Tipo de usuario (admin o user): ")
    if user_type not in ['admin', 'user']:
        limpiar_consola()
        print("\n-> Tipo de usuario no válido. Debe ser 'admin' o 'user'.")
        return
    if db.user_exists(username):
        limpiar_consola()
        print("\n -> El usuario ya existe. Elija otro nombre de usuario.")
    else:
        db.insert_usuario(username, password, user_type)
        limpiar_consola()
        print(f"\n -> Registro exitoso como {user_type}. <-")
def login_user(db):
    print("\n -> Opcion de iniciar sesión.")
    username = input("\n<- Usuario: ")
    password = input("<- Contraseña: ")
    user_type = db.authenticate(username, password)
    if user_type == 'admin':
        admin = Admin(username)
        limpiar_consola()
        worker_menu(admin, db)
    elif user_type == 'user':
        work = Work(username)
        limpiar_consola()
        work_menu(work, db)
    else:
        limpiar_consola()
        print("\n -> Nombre de usuario o contraseña incorrectos.")
def worker_menu(admin, db):
    while True:
        print(f"\n -> Bienvenido, {admin.get_username()} (Administrador) <-")
        print("\n1. Realizar acciones para trabajadores")
        print("2. Salir")
        opcion = input("\n <- Elija una opción: ")
        if opcion == "1":
            limpiar_consola()
            admin.perform_action(db)
        elif opcion == "2":
            limpiar_consola()
            break
        else:
            limpiar_consola()
            print("\n -> Opción no válida. Intente de nuevo.")
def work_menu(work, db):
    while True:
        print(f"\n -> Bienvenido, {work.get_username()} (Usuario) <-")
        print("\n1. Realizar acción para trabajos")
        print("2. Salir")
        opcion = input("\n <- Elija una opción: ")
        if opcion == "1":
            limpiar_consola()
            work.perform_action(db)
        elif opcion == "2":
            limpiar_consola()
            break
        else:
            limpiar_consola()
            print("\n -> Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()