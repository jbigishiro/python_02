class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        book.set_library(self)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.library = None

    def set_library(self, library):
        self.library = library

# Create library instances
library1 = Library("Main Library")
library2 = Library("Branch Library")

# Create book instances
book1 = Book("Python Programming", "John Doe")
book2 = Book("Introduction to Algorithms", "Jane Smith")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Add books to libraries
library1.add_book(book1)
library1.add_book(book2)
library2.add_book(book3)

# Print library and book information
for library in [library1, library2]:
    print(f"Library: {library.name}")
    if library.books:
        print("Books:")
        for book in library.books:
            print(f"- {book.title} by {book.author}")
    else:
        print("No books available\n")

    print()
