import sqlite3
from errors import UnspecifiedDataError


class PasswordDatabase():
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.__create_table__()
    
           
    def __create_table__(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                            service TEXT,
                            username TEXT,
                            password TEXT
                        )''')
        self.connection.commit()
        
        
    
    def save_data(self, new_data:tuple):
        website, username, password = new_data
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?)", (website, username, password))
        self.connection.commit()
        
    
    def get_password(self, website, username):
        self.cursor.execute("SELECT password FROM passwords WHERE service = ? AND username = ?", (website, username))
        result = self.cursor.fetchone()
        return result[0] if result else None