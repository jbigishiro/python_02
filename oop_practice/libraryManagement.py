# Exercise: Create a Library Management System

# Create a class called Book.

# The class should have the following attributes:

# book_id (a unique identifier for each book).
# title (the title of the book).
# author (the author of the book).
# is_borrowed (a boolean indicating whether the book is currently borrowed or not).
# The class should have the following methods:

# display_book_info(): Displays information about the book (book_id, title, author, and status - borrowed or available).
# Create a class called User.

# The class should have the following attributes:

# user_id (a unique identifier for each user).
# name (the name of the user).
# The class should have the following methods:

# display_user_info(): Displays information about the user (user_id and name).
# Create a class called Library.

# The class should have the following attributes:

# books (a list to store all the books in the library).
# users (a list to store all the users registered in the library).
# borrowed_books (a dictionary to keep track of books borrowed by users).
# The class should have the following methods:

# add_book(book): Adds a book to the library.
# remove_book(book_id): Removes a book from the library based on its book_id.
# add_user(user): Adds a user to the library.
# remove_user(user_id): Removes a user from the library based on their user_id.
# borrow_book(user_id, book_id): Allows a user to borrow a book from the library.
# return_book(user_id, book_id): Allows a user to return a borrowed book to the library.
# display_books(): Displays information about all the books in the library.
# display_users(): Displays information about all the users in the library.
# display_borrowed_books(): Displays information about borrowed books and their borrowers.
# Test your classes by creating instances of Book, User, and Library. Perform various library operations, such as adding/removing books, adding/removing users, borrowing/returning books, and displaying library information.

# Example Usage:

# python
# Copy code
# # Create book instances
# book1 = Book(1, 'Python Crash Course', 'Eric Matthes')
# book2 = Book(2, 'Deep Learning', 'Ian Goodfellow')

# # Create user instances
# user1 = User(101, 'John Doe')
# user2 = User(102, 'Jane Smith')

# # Create library instance
# library = Library()

# # Add books to the library
# library.add_book(book1)
# library.add_book(book2)

# # Add users to the library
# library.add_user(user1)
# library.add_user(user2)

# # Borrow books from the library
# library.borrow_book(101, 1)
# library.borrow_book(102, 2)

# # Display borrowed books and their borrowers
# library.display_borrowed_books()

# # Return books to the library
# library.return_book(101, 1)
# library.return_book(102, 2)

# # Display information about books and users in the library
# library.display_books()
# library.display_users()
# Expected Output:

# yaml
# Copy code
# Books Borrowed:
# Book ID: 1, Title: Python Crash Course, Borrower: John Doe
# Book ID: 2, Title: Deep Learning, Borrower: Jane Smith

# All Books in Library:
# Book ID: 1, Title: Python Crash Course, Author: Eric Matthes, Status: Available
# Book ID: 2, Title: Deep Learning, Author: Ian Goodfellow, Status: Available

# All Users in Library:
# User ID: 101, Name: John Doe
# User ID: 102, Name: Jane Smith
# In this exercise, we created three classes: Book, User, and Library. The Book class represents individual books with attributes (book_id, title, author, and is_borrowed). The User class represents library users with attributes (user_id and name). The Library class serves as the library management system and contains methods for managing books, users, and borrowing operations.

# The example usage demonstrates how to create instances of Book, User, and Library, add books and users to the library, allow users to borrow books, return books, and display information about the books and users in the library.

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def display_user_info(self):
        print(f"User ID: {self.user_id}, Name: {self.name}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]

    def borrow_book(self, user_id, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_borrowed:
                book.is_borrowed = True
                self.borrowed_books[book_id] = user_id
                print(f"{book.title} has been borrowed by user {user_id}.")
                return
        print("Book not available for borrowing.")

    def return_book(self, user_id, book_id):
        if book_id in self.borrowed_books and self.borrowed_books[book_id] == user_id:
            for book in self.books:
                if book.book_id == book_id:
                    book.is_borrowed = False
                    del self.borrowed_books[book_id]
                    print(f"{book.title} has been returned.")
                    return
        print("Invalid return. Book not borrowed by the given user.")

    def display_books(self):
        print("All Books in Library:")
        for book in self.books:
            book.display_book_info()

    def display_users(self):
        print("All Users in Library:")
        for user in self.users:
            user.display_user_info()

    def display_borrowed_books(self):
        print("Books Borrowed:")
        for book_id, user_id in self.borrowed_books.items():
            for book in self.books:
                if book.book_id == book_id:
                    print(f"Book ID: {book_id}, Title: {book.title}, Borrower: {user_id}")
                    break


# Example Usage
book1 = Book(1, 'Python Crash Course', 'Eric Matthes')
book2 = Book(2, 'Deep Learning', 'Ian Goodfellow')

user1 = User(101, 'John Doe')
user2 = User(102, 'Jane Smith')

library = Library()

library.add_book(book1)
library.add_book(book2)

library.add_user(user1)
library.add_user(user2)

library.borrow_book(101, 1)
library.borrow_book(102, 2)

library.display_borrowed_books()

library.return_book(101, 1)
library.return_book(102, 2)

library.display_books()
library.display_users()
