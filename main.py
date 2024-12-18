import json 
import datetime 

class Book: 
    #Todo: Add books

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book, due_date):
        if book.quantity > 0:
            self.borrowed_books[book.isbn] = {'book': book, 'due_date': due_date}
            book.quantity -= 1
            print(f"{self.name} borrowed {book.title} (Due Date: {due_date})")
        else:
            print(f"{book.title} is currently unavailable for borrowing.")

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            del self.borrowed_books[book.isbn]
            book.quantity += 1
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} has not borrowed {book.title}.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book_info in self.borrowed_books.values():
                book = book_info['book']
                due_date = book_info['due_date']
                print(f"{book.title}, Due Date: {due_date}")
        else:
            print(f"{self.name} has no borrowed books.")

class Library: 
    #Todo: Add library functions
