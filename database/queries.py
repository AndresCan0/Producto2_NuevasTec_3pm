#queries.py
import sqlite3, os

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Queries:
    @staticmethod
    def get_sorted_workers(db):
        try:
            limpiar_consola()
            print("\n-> Ver Trabajadores registrados <-\n")
            db.cursor.execute("SELECT * FROM trabajadores ORDER BY NombreTrabajador")
            result = db.cursor.fetchall()
            for row in result:
                print(row)
            input("\n enter para continuar ")
        except sqlite3.Error as e:
            print(f"Error al obtener trabajadores: {e}")
    @staticmethod
    def get_work_with_boss(db):
        try:
            limpiar_consola()
            print("\n-> Ver trabajos registrados <-\n")
            db.cursor.execute("SELECT * FROM trabajo ORDER BY JefeTrabajo")
            result = db.cursor.fetchall()
            for row in result:
                print(row)
            input("\n enter para continuar ")
        except sqlite3.Error as e:
            print(f"Error al obtener nombre del trabajo: {e}")

            