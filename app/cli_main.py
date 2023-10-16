from PasswordManager import PasswordManager
from PasswordDatabase import PasswordDatabase
import getpass

myPasswordManager = PasswordManager('key.key', 'passwords.txt')
myPasswordManager.save_password_txt(service='website', username='google', password='12356')
myPasswordDatabase = PasswordDatabase('passwords.db', 'passwords')
tempdata = ('website', 'google', '123456')



while True:
    print("\nPassword Manager Menu:")
    print("1. Save Password")
    print("2. Get Password")
    print("3. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        service = input("Enter the service or website name: ")
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        myPasswordManager.save_password_txt(service, username, password)
        myPasswordDatabase.save_data((service, username, myPasswordManager.encrypt_pass(password)))
        print("Password saved successfully!")

    elif choice == '2':
        service = input("Enter the service or website name: ")
        username = input("Enter your username: ")
        password = myPasswordManager.get_password(service, username)
        if password:
            print(f"Password: {password}")
        else:
            print("Password not found!")

    elif choice == '3':
        myPasswordDatabase.close_connection()
        break