import sqlite3
from errors import UnspecifiedDataError


class PasswordDatabase():
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.__create_table__(self)
    
           
    def __create_table__(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                            service TEXT,
                            username TEXT,
                            password TEXT
                        )''')
        self.connection.commit()
        
    
    def save_data(self, new_data:tuple):
        website, username, password = new_data
        query = f"INSERT INTO {self.table_name} VALUES {website}, ?, ?)"
        self.cursor.execute(query)
        self.cursor.commit()
    
    def retrieve_data(self, data):
        pass
            
    def retrieve_data(self, what_to_retrieve:str):
        pass
            