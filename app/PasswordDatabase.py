import sqlite3
from errors import *


class PasswordDatabase():
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.__create_table__()
    
           
    def __create_table__(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                            service TEXT,
                            username TEXT,
                            password TEXT
                        )''')
        self.connection.commit()
        
    
    def save_data(self, new_data:tuple):
        website, username, password = new_data
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?)", (website, username, password))
        self.connection.commit()
    
    def list_all_website_with_username(self, username: str):
        self.cursor.execute(f"SELECT service FROM {self.table_name} WHERE username = (?)", username)
        result = self.cursor.fetchall()
        if len(result) > 0:
            return result
        raise EmptyResponseError("Empty result received")
    
    def list_all_website_or_username(self, website_or_username:str):
        if website_or_username == 'website':
            self.cursor.execute(f"SELECT service FROM {self.table_name}")
        elif(website_or_username == 'username'):
            self.cursor.execute(f"SELECT username FROM {self.table_name}")
        else:
            return None
        result = self.cursor.fetchall()
        if len(result > 0):
            return result
        else: raise EmptyResponseError("Empty result received")

    def close_connection(self):
        self.connection.close()