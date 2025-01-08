import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
from pymongo import MongoClient

# Class to represent a Book entity
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.due_date = None  # Initialize due_date as None

# Class to represent a User entity
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

# Main Library Management System Class with the GUI
class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x600")  # Set window size

        # Connect to MongoDB
        self.client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB database
        self.db = self.client["library_db"]  # Access the library database
        self.books_collection = self.db["books"]  # Collection to store books data
        self.users_collection = self.db["users"]  # Collection to store user data
        self.borrowed_books_collection = self.db["borrowed_books"]  # Collection to track borrowed books
        self.initialize_database()  # Function to initialize any database-specific setup

        # Apply modern ttk styles for buttons and labels
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Helvetica", 10))
        self.style.configure("TLabel", font=("Helvetica", 12), padding=6)

        # Create the GUI elements
        self.create_widgets()

    def initialize_database(self):
        # MongoDB automatically handles collections and indexes, so no need for schema creation.
        pass

    def create_widgets(self):
        # Create frames to organize sections of the interface for adding books, borrowing, returning, etc.
        self.frame1 = ttk.LabelFrame(self.root, text="Add Book", padding=(20, 10))
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.frame2 = ttk.LabelFrame(self.root, text="Borrow Book", padding=(20, 10))
        self.frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.frame3 = ttk.LabelFrame(self.root, text="Return Book", padding=(20, 10))
        self.frame3.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.frame4 = ttk.LabelFrame(self.root, text="Search Book", padding=(20, 10))
        self.frame4.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.frame5 = ttk.LabelFrame(self.root, text="Manage User Records", padding=(20, 10))
        self.frame5.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Add Book Section: Collect title, author, and ISBN for new books
        ttk.Label(self.frame1, text="Book Title:").grid(row=0, column=0, sticky="w")
        self.book_title_entry = ttk.Entry(self.frame1, width=30)
        self.book_title_entry.grid(row=0, column=1, padx=10)

        ttk.Label(self.frame1, text="Author Name:").grid(row=1, column=0, sticky="w")
        self.book_author_entry = ttk.Entry(self.frame1, width=30)
        self.book_author_entry.grid(row=1, column=1, padx=10)

        ttk.Label(self.frame1, text="ISBN:").grid(row=2, column=0, sticky="w")
        self.book_isbn_entry = ttk.Entry(self.frame1, width=30)
        self.book_isbn_entry.grid(row=2, column=1, padx=10)

        # Button to add the new book to the database
        self.add_book_button = ttk.Button(self.frame1, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Borrow Book Section: Collect user ID and ISBN to borrow a book
        ttk.Label(self.frame2, text="User ID:").grid(row=0, column=0, sticky="w")
        self.user_id_entry = ttk.Entry(self.frame2, width=30)
        self.user_id_entry.grid(row=0, column=1, padx=10)

        ttk.Label(self.frame2, text="Book ISBN:").grid(row=1, column=0, sticky="w")
        self.book_isbn_borrow_entry = ttk.Entry(self.frame2, width=30)
        self.book_isbn_borrow_entry.grid(row=1, column=1, padx=10)

        # Button to borrow a book
        self.borrow_book_button = ttk.Button(self.frame2, text="Borrow Book", command=self.borrow_book)
        self.borrow_book_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Return Book Section: Collect the ISBN to return a borrowed book
        ttk.Label(self.frame3, text="Book ISBN:").grid(row=0, column=0, sticky="w")
        self.book_isbn_return_entry = ttk.Entry(self.frame3, width=30)
        self.book_isbn_return_entry.grid(row=0, column=1, padx=10)

        # Button to return a book
        self.return_book_button = ttk.Button(self.frame3, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Search Book Section: Allows searching for books by title or author
        ttk.Label(self.frame4, text="Search Term:").grid(row=0, column=0, sticky="w")
        self.search_book_entry = ttk.Entry(self.frame4, width=30)
        self.search_book_entry.grid(row=0, column=1, padx=10)

        # Button to search for books
        self.search_book_button = ttk.Button(self.frame4, text="Search Book", command=self.search_book)
        self.search_book_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Manage User Records Section: View all user records and borrowed books
        self.view_user_button = ttk.Button(self.frame5, text="View User Records", command=self.view_user_records)
        self.view_user_button.grid(row=0, column=0, columnspan=2, pady=10)

    # Function to add a new book to the database
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        isbn = self.book_isbn_entry.get()

        if title and author and isbn:
            # Insert book details into the books collection
            book = {
                "isbn": isbn,
                "title": title,
                "author": author,
                "available": True,
                "due_date": None
            }
            self.books_collection.insert_one(book)
            messagebox.showinfo("Success", f"Book '{title}' added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # Function to borrow a book
    def borrow_book(self):
        user_id = self.user_id_entry.get()
        isbn = self.book_isbn_borrow_entry.get()

        if user_id and isbn:
            # Find the book with the specified ISBN
            book = self.books_collection.find_one({"isbn": isbn})

            # Check if the book is available for borrowing
            if book and book["available"]:
                # Check if the user exists, if not, create a new user record
                user = self.users_collection.find_one({"user_id": user_id})

                if not user:
                    self.users_collection.insert_one({"user_id": user_id, "name": user_id})

                # Set the due date to 7 days from now
                due_date = datetime.now() + timedelta(days=7)

                # Update the book's availability and set the due date
                self.books_collection.update_one({"isbn": isbn}, {"$set": {"available": False, "due_date": due_date}})
                # Record the borrowed book in the borrowed_books collection
                self.borrowed_books_collection.insert_one({"user_id": user_id, "isbn": isbn})

                messagebox.showinfo("Success", "Book borrowed successfully.")
            else:
                messagebox.showerror("Error", "Book not available or not found.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # Function to return a borrowed book
    def return_book(self):
        isbn = self.book_isbn_return_entry.get()

        if isbn:
            # Find the book with the specified ISBN
            book = self.books_collection.find_one({"isbn": isbn})

            if book:
                # Remove the book from borrowed_books collection and update its availability
                self.borrowed_books_collection.delete_one({"isbn": isbn})
                self.books_collection.update_one({"isbn": isbn}, {"$set": {"available": True, "due_date": None}})
                messagebox.showinfo("Success", "Book returned successfully.")
            else:
                messagebox.showerror("Error", "Book not found.")
        else:
            messagebox.showerror("Error", "Please fill in the book ISBN.")

    # Function to search for books by title or author
    def search_book(self):
        search_term = self.search_book_entry.get()

        if search_term:
            # Search for books matching the search term
            results = self.books_collection.find({
                "$or": [
                    {"title": {"$regex": search_term, "$options": "i"}},
                    {"author": {"$regex": search_term, "$options": "i"}}
                ]
            })

            result_str = ""
            for book in results:
                result_str += f"Title: {book['title']}, Author: {book['author']}, Available: {'Yes' if book['available'] else 'No'}\n"

            if result_str:
                messagebox.showinfo("Search Results", result_str)
            else:
                messagebox.showinfo("No Results", "No books found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    # Function to view user records and borrowed books
    def view_user_records(self):
        users = self.users_collection.find()
        borrowed_books = self.borrowed_books_collection.find()

        user_str = "User Records:\n"
        for user in users:
            user_str += f"User ID: {user['user_id']}, Name: {user['name']}\n"

        borrowed_str = "Borrowed Books:\n"
        for borrowed in borrowed_books:
            book = self.books_collection.find_one({"isbn": borrowed['isbn']})
            borrowed_str += f"User ID: {borrowed['user_id']}, Book: {book['title']}\n"

        messagebox.showinfo("User Records", user_str + "\n" + borrowed_str)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
