# worker.py
import os
from users.user import User
from database.queries import Queries

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Admin(User):
    def perform_action(self, db):
        while True:
            limpiar_consola()
            print("\n-> Realizar acciones para trabajadores <-\n")
            print("1. Agregar trabajador")
            print("2. Ver todos los trabajadores registrados")
            print("3. Eliminar trabajador de la base de datos")
            print("4. Salir")
            opcion = input("\n <- Elija una opción: ")
            if opcion == "1":
                idtrabajador = input("\nId trabajador: ")
                NombreTrabajador = input("Nombre trabajador: ")
                Especialidad = input("Especialidad: ")
                TrabajoActual = input("Trabajo Actual: ")
                db.insert_worker(idtrabajador, NombreTrabajador, Especialidad, TrabajoActual)
            elif opcion == "2":
                Queries.get_sorted_workers(db)
            elif opcion == "3":
                limpiar_consola()
                id_trabajador = input("\n <- Id del trabajador a eliminar: ")
                db.delete_worker(id_trabajador,)
            elif opcion == "4":
                limpiar_consola()
                break
            else:
                limpiar_consola()
                print("\n -> Opción no válida. Intente de nuevo.")