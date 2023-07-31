# Exercise: Expand Library Management System with Book Search

# Extend the Library class with the following method:

# search_by_title(title): Allows users to search for books in the library by title. This method should display all books whose titles contain the given title (case-insensitive).
# Extend the Library class with the following method:

# search_by_author(author): Allows users to search for books in the library by author. This method should display all books whose authors contain the given author (case-insensitive).
# Test your classes by creating instances of Book, User, and Library. Add some books and users to the library. Perform various library operations, such as borrowing/returning books, displaying library information, and searching for books by title and author.

# Example Usage:

# python
# Copy code
# # Create book instances
# book1 = Book(1, 'Python Crash Course', 'Eric Matthes')
# book2 = Book(2, 'Deep Learning', 'Ian Goodfellow')
# book3 = Book(3, 'The Great Gatsby', 'F. Scott Fitzgerald')

# # Create user instances
# user1 = User(101, 'John Doe')
# user2 = User(102, 'Jane Smith')

# # Create library instance
# library = Library()

# # Add books to the library
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

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

# # Search for books by title and author
# print("\nBooks containing 'Python' in the title:")
# library.search_by_title('Python')

# print("\nBooks by author 'Fitzgerald':")
# library.search_by_author('Fitzgerald')
# Expected Output:

# yaml
# Copy code
# Python Crash Course has been borrowed by user 101.
# Deep Learning has been borrowed by user 102.
# Books Borrowed:
# Book ID: 1, Title: Python Crash Course, Borrower: 101
# Book ID: 2, Title: Deep Learning, Borrower: 102
# Python Crash Course has been returned.
# Deep Learning has been returned.
# All Books in Library:
# Book ID: 1, Title: Python Crash Course, Author: Eric Matthes, Status: Available
# Book ID: 2, Title: Deep Learning, Author: Ian Goodfellow, Status: Available
# Book ID: 3, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Status: Available
# All Users in Library:
# User ID: 101, Name: John Doe
# User ID: 102, Name: Jane Smith

# Books containing 'Python' in the title:
# Book ID: 1, Title: Python Crash Course, Author: Eric Matthes, Status: Available

# Books by author 'Fitzgerald':
# Book ID: 3, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Status: Available
# In this exercise, we extended the Library class with two additional methods: search_by_title(title) and search_by_author(author). These methods allow users to search for books in the library by title or author and display the matching results.

# The example usage demonstrates how to create instances of Book, User, and Library, add books and users to the library, allow users to borrow books, return books, display information about the books and users in the library, and search for books by title and author.

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

    def search_by_title(self, title):
        print(f"Books containing '{title}' in the title:")
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                book.display_book_info()
        else:
            print("No books found with the given title.")

    def search_by_author(self, author):
        print(f"Books by author '{author}':")
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                book.display_book_info()
        else:
            print("No books found by the given author.")


# Example Usage
book1 = Book(1, 'Python Crash Course', 'Eric Matthes')
book2 = Book(2, 'Deep Learning', 'Ian Goodfellow')
book3 = Book(3, 'The Great Gatsby', 'F. Scott Fitzgerald')

user1 = User(101, 'John Doe')
user2 = User(102, 'Jane Smith')

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_user(user1)
library.add_user(user2)

library.borrow_book(101, 1)
library.borrow_book(102, 2)

library.display_borrowed_books()

library.return_book(101, 1)
library.return_book(102, 2)

library.display_books()
library.display_users()

library.search_by_title('Python')
library.search_by_author('Fitzgerald')
