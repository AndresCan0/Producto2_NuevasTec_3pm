import pymysql

class DBConnection:
    
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password', 
            db='bikestore'
        )

    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def close(self):
        self.connection.close()