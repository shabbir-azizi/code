# Library Management System

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (Copies: {self.copies})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available books in the library:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f"You have successfully borrowed '{book.title}'.")
                return
        print(f"Sorry, '{title}' is not available or out of stock.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Thank you for returning '{book.title}'.")
                return
        print(f"'{title}' does not belong to this library.")


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a Book")
        print("2. View Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")







