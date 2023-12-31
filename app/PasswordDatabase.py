import sqlite3
from errors import *


class PasswordDatabase():
    def __init__(self, db_name):
        self.db_name = db_name
        self.table_names = ('usernames', 'websites', 'passwords')
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.__create_all_tables__()
    
    def __create_all_tables(self):
        self.__create_website_table___()
        self.__create_usernames_table__()
        self.__create_passwords_table__()


    def __create_website_table___(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_names[1]} (
                            ID INTEGER PRIMARY KEY,
                            website TEXT
                        )''')
        self.connection.commit()
        
        
    
    def save_data(self, new_data:tuple):
        website, username, password = new_data
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?)", (website, username, password))
        self.connection.commit()
        
    
    def list_all_website_with_single_username(self, username: str):
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
        else:
            raise EmptyResponseError("Empty result received")
            

    def update_username(self, new_username:str, website:str):
        self.cursor.execute(f"SELECT username FROM {self.table_name} WHERE service =(?)",website)
        result = self.cursor.fetchone()
        if len(result) == len(list()):
            raise NoDataAvailableException("No data found by this website")
        else:
            query = "UPDATE passwords SET username = (?) WHERE service = (?)"
            self.cursor.execute(query, (new_username, website))
            self.connection.commit()

    def update_password(self, new_password, username):
        query = "UPDATE passwords SET password = (?) WHERE username = (?)"
        self.cursor.execute(query, (new_password, username ))
        self.connection.commit()

    def remove_username(self, username):
        pass
    
    def close_connection(self):
        self.connection.close()
    
    @staticmethod
    def get_const():
        '''For testing purposes
        Testing if the import into pytest is working
        '''
        return 1
    @staticmethod
    def get_const2():
        return 2