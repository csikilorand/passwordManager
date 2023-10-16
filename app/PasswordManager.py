from cryptography.fernet import Fernet
import os


class PasswordManager:
    def __init__(self, key_file, password_file):
        self.key_file = key_file
        self.password_file = password_file
        self.key = self.load_or_generate_key()
        

    def load_or_generate_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
        else:
            with open(self.key_file, 'rb') as file:
                key = file.read()
        return key

    def save_password_txt(self, service, username, password):
        fernet = Fernet(self.key)
        encrypted_password = fernet.encrypt(password.encode())
        with open(self.password_file, 'a') as file:
            file.write(f"{service}:{username}:{encrypted_password.decode()}\n")
    def encrypt_pass(self, password)-> str:
        fernet = Fernet(self.key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password.decode()

    def get_password(self, service, username):
        fernet = Fernet(self.key)
        with open(self.password_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 3 and parts[0] == service and parts[1] == username:
                    encrypted_password = parts[2]
                    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                    return decrypted_password
        return None
    