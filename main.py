import json 
import datetime 

class Book: 
    #Todo: Add books

class User: 
    #Todo: Add users 

class Library: 
    def __init__(self):
        self.books = []
        self.users = {}

        # Load data from JSON files
        self.load_books()
        self.load_users()

   
