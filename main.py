import json 
import datetime 

class Book: 
    #Todo: Add books

class User: 
    #Todo: Add users 

class Library: 
    class Library:
    def __init__(self):
        self.books = []
        self.users = {}

        # Load data from JSON files
        self.load_books()
        self.load_users()

    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                books_data = json.load(file)
                self.books = [Book(book['title'], book['author'], book['isbn'], book['quantity']) for book in books_data]
        except FileNotFoundError:
            print("Books data file not found. Starting with an empty collection.")
    
    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                users_data = json.load(file)
                self.users = {user['user_id']: User(user['user_id'], user['name']) for user in users_data}
        except FileNotFoundError:
            print("Users data file not found. Starting with no registered users.")

    def save_books(self):
        with open('books.json', 'w') as file:
            books_data = [book.to_dict() for book in self.books]
            json.dump(books_data, file, indent=4)

    def save_users(self):
        with open('users.json', 'w') as file:
            users_data = [{'user_id': user.user_id, 'name': user.name} for user in self.users.values()]
            json.dump(users_data, file, indent=4)

    def add_book(self, title, author, isbn, quantity):
        new_book = Book(title, author, isbn, quantity)
        self.books.append(new_book)
        print(f"Added {title} to the library.")
        self.save_books()

    def remove_book(self, isbn):
        book_to_remove = self.find_book_by_isbn(isbn)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Removed {book_to_remove.title} from the library.")
            self.save_books()
        else:
            print(f"Book with ISBN {isbn} not found.")

    def update_book(self, isbn, title=None, author=None, quantity=None):
        book_to_update = self.find_book_by_isbn(isbn)
        if book_to_update:
            if title: book_to_update.title = title
            if author: book_to_update.author = author
            if quantity is not None: book_to_update.quantity = quantity
            print(f"Updated book details for {book_to_update.title}.")
            self.save_books()
        else:
            print(f"Book with ISBN {isbn} not found.")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_books(self, title=None, author=None, isbn=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (isbn and isbn == book.isbn):
                results.append(book)
        return results

    def register_user(self, user_id, name):
        if user_id not in self.users:
            new_user = User(user_id, name)
            self.users[user_id] = new_user
            print(f"Registered new user: {name}")
            self.save_users()
        else:
            print(f"User with ID {user_id} is already registered.")

    def borrow_book(self, user_id, isbn):
        user = self.users.get(user_id)
        if not user:
            print(f"User with ID {user_id} not found.")
            return

        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return

        # Calculate due date (14 days from today)
        due_date = datetime.date.today() + datetime.timedelta(days=14)
        user.borrow_book(book, due_date)

    def return_book(self, user_id, isbn):
        user = self.users.get(user_id)
        if not user:
            print(f"User with ID {user_id} not found.")
            return

        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return

        user.return_book(book)

    def overdue_books(self):
        today = datetime.date.today()
        overdue = []
        for user in self.users.values():
            for book_info in user.borrowed_books.values():
                due_date = book_info['due_date']
                if due_date < today:
                    overdue.append((user.name, book_info['book'].title, due_date))
        return overdue

    def notify_overdue(self):
        overdue = self.overdue_books()
        if overdue:
            print("Overdue Books Notifications:")
            for user_name, book_title, due_date in overdue:
                print(f"{user_name}'s borrowed {book_title} (Due Date: {due_date}) is overdue!")
        else:
            print("No overdue books.")

