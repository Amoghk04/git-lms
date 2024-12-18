import json 
import datetime 

class Book: 
    #Todo: Add books

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = {}

class Library: 
    def __init__(self):
        self.books = []
        self.users = {}

        # Load data from JSON files
        self.load_books()
        self.load_users()

   

    #user related functions
    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                users_data = json.load(file)
                self.users = {user['user_id']: User(user['user_id'], user['name']) for user in users_data}
        except FileNotFoundError:
            print("Users data file not found. Starting with no registered users.")
    def save_users(self):
        with open('users.json', 'w') as file:
            users_data = [{'user_id': user.user_id, 'name': user.name} for user in self.users.values()]
            json.dump(users_data, file, indent=4)


    def register_user(self, user_id, name):
        if user_id not in self.users:
            new_user = User(user_id, name)
            self.users[user_id] = new_user
            print(f"Registered new user: {name}")
            self.save_users()
        else:
            print(f"User with ID {user_id} is already registered.")
