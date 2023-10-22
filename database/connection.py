#connection.py
import sqlite3, os

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class DataBase:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def connect(self):
        self.connection = sqlite3.connect('Workers.db')
        self.cursor = self.connection.cursor()
        limpiar_consola()
        print("\n -> Conexión a la base de datos exitosa <-")
        self.create_tables()
    def close(self):
        if self.connection:
            self.connection.close()
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trabajadores (
                idtrabajador INTEGER PRIMARY KEY,
                NombreTrabajador TEXT NOT NULL,
                Especialidad TEXT NOT NULL,
                TrabajoActual TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trabajo (
                JefeTrabajo TEXT NOT NULL,
                NombreTrabajo TEXT NOT NULL,
                Localizacion INTEGER NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    def authenticate(self, username, password):
        try:
            self.cursor.execute("SELECT user_type FROM usuarios WHERE username = ? AND password = ?", (username, password))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"\n <- Error al autenticar al usuario: {e}")
            return None

    def user_exists(self, username):
        try:
            self.cursor.execute("SELECT username FROM usuarios WHERE username = ?", (username,))
            result = self.cursor.fetchone()
            return result is not None
        except sqlite3.Error as e:
            print(f"\n <- Error al verificar si el usuario existe: {e}")
            return False
    def insert_worker(self, idTrabajador, NombreTrabajador, Especialidad, TrabajoActual):
        try:
            self.cursor.execute("INSERT INTO trabajadores (idTrabajador, NombreTrabajador, Especialidad, TrabajoActual) VALUES (?, ?, ?, ?)", (idTrabajador, NombreTrabajador, Especialidad, TrabajoActual))
            self.connection.commit()
            print(f"\n -> Trabajador {NombreTrabajador} agregado a la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar el Trabajador: {e}")
            
    def insert_usuario(self, username, password, user_type):
        try:
            self.cursor.execute("INSERT INTO usuarios (username, password, user_type) VALUES (?, ?, ?)", (username, password, user_type))
            self.connection.commit()
            print(f"\n -> Usuario {username} registrado en la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar usuario: {e}")
    def insert_work(self, JefeTrabajo, NombreTrabajo, Localizacion):
        try:
            self.cursor.execute("INSERT INTO trabajo (JefeTrabajo, NombreTrabajo, Localizacion) VALUES (?, ?, ?)", (JefeTrabajo, NombreTrabajo, Localizacion))
            self.connection.commit()
            print(f"\n -> Trabajo {NombreTrabajo} agregado a la base de datos <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar el trabajo: {e}")
    def delete_work(self, NombreTrabajo):
        try:
            self.cursor.execute("DELETE FROM trabajo WHERE NombreTrabajo = ?", (NombreTrabajo,))
            self.connection.commit()
            print(f"\n -> Trabajo {NombreTrabajo} eliminado de la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al eliminar el trabajo: {e}")
    def delete_worker(self, idtrabajador):
        try:
            self.cursor.execute("DELETE FROM trabajadores WHERE idtrabajador = ?", (idtrabajador,))
            self.connection.commit()
            print(f"\n -> Trabajador con id {idtrabajador} eliminado de la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al eliminar el Trabajador: {e}")