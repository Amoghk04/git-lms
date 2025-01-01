# Library Management System

A simple library management system written in Python, designed to manage books, users, and their borrowing activities. It includes functionalities to add, remove, and search for books, as well as manage user registrations, borrowing, and returning of books. The system stores data in JSON files for books and users.

## Features

- **Book Management**:
  - Add new books to the library.
  - Remove books from the library.
  - Update book details (e.g., quantity, title, author).
  - Search books by title, author, or ISBN.

- **User Management**:
  - Register new users.
  - Borrow books from the library.
  - Return borrowed books.
  - List borrowed books for each user.

## Classes

### 1. `Book`
This class represents a book in the library. It stores details such as the title, author, ISBN, and quantity. It has methods for:
- Converting the book object to a dictionary for JSON serialization.
- Returning a string representation of the book.

### 2. `User`
This class represents a user of the library. It stores details such as user ID, name, and borrowed books. It has methods for:
- Borrowing books with due dates.
- Returning borrowed books.
- Listing borrowed books.

### 3. `Library`
This class manages the collection of books and users. It supports functionalities like:
- Adding, removing, and updating books.
- Registering users.
- Borrowing and returning books.
- Checking for overdue books and sending notifications.

---

## Usage
- Clone the repo and run main.py
