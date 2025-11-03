class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"'{title}' is currently not available.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
