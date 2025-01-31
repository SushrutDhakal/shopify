class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self._is_available = True
        self._borrowed_by = None

    def borrow(self, user):
        if self._is_available:
            self._is_available = False
            self._borrowed_by = user.name
            return f"{user.name} borrowed '{self.title}'."
        return f"'{self.title}' is not available."

    def return_book(self):
        if not self._is_available:
            borrower = self._borrowed_by
            self._is_available = True
            self._borrowed_by = None
            return f"'{self.title}' returned by {borrower}."
        return f"'{self.title}' was not borrowed."

    def is_available(self):
        return self._is_available

    def borrowed_by(self):
        return self._borrowed_by


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            self.borrowed_books.append(book)
            return book.borrow(self)
        return f"{self.name} cannot borrow '{book.title}' as it is unavailable."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return book.return_book()
        return f"{self.name} does not have '{book.title}'."

    def borrowed_count(self):
        return len(self.borrowed_books)


class RegularMember(User):
    MAX_BOOKS = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            return f"{self.name} has reached the borrowing limit ({self.MAX_BOOKS} books)."
        return super().borrow_book(book)


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        return f"{self.name} added '{book.title}' to the library."

    def remove_book(self, library, book):
        return library.remove_book(book)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books and book.is_available():
            self.books.remove(book)
            return f"'{book.title}' removed from the library."
        return f"Cannot remove '{book.title}' as it is currently borrowed."

    def search_books(self, keyword):
        matches = [book for book in self.books if keyword.lower() in book.title.lower() or 
                   keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower()]
        return matches if matches else f"No books found for '{keyword}'."

    def display_status(self):
        available_books = [book.title for book in self.books if book.is_available()]
        borrowed_books = [(book.title, book.borrowed_by()) for book in self.books if not book.is_available()]

        return {
            "Available Books": available_books,
            "Borrowed Books": borrowed_books
        }