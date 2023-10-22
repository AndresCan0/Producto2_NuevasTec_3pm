# work.py
import os
from users.user import User
from database.queries import Queries

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Work(User):
    def perform_action(self, db):
        while True:
            limpiar_consola()
            print("\n-> Realizar acciones para trabajos <-\n")
            print("1. Agregar trabajo")
            print("2. Ver todos los trabajos Disponibles")
            print("3. Eliminar trabajos de la base de datos")
            print("4. Salir")
            opcion = input("\n <- Elija una opción: ")
            if opcion == "1":
                JefeTrabajo = input("\Jefe a cargo: ")
                NombreTrabajo = input("Nombre: ")
                Localizacion = input("Localizacion: ")
                db.insert_work(JefeTrabajo, NombreTrabajo, Localizacion)
            elif opcion == "2":
                Queries.get_work_with_boss(db)
            elif opcion == "3":
                limpiar_consola()
                nombre_trabajo = input("\n <- Nombre del trabajo a eliminar: ")
                db.delete_work(nombre_trabajo)
            elif opcion == "4":
                limpiar_consola()
                break
            else:
                limpiar_consola()
                print("\n -> Opción no válida. Intente de nuevo.")