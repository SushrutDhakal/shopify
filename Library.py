class Book:
    def __init__(self, title, author, genre, id):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id 
        self.is_avaliable = True 
        self.borrowed_by = None

class User:
    def __init__(self, user_type, name):
        self.user_type = user_type
        self.name = name
        self.book_count = 0

class Library:

    def __init__(self):
        self.books = []

    def borrow_book(self, book, user):
        if user.user_type == "Regular Member":
            if user.book_count < 3:
                if book in self.books and book.is_avaliable:
                    book.is_avaliable = False 
                    user.book_count += 1
                else:
                    return f"{book.title} is not avaliable in the library"
            else:
                return f"As a {user.user_type} you can only borrow 3 books total."
        else: 
            book.is_avaliable = False 
            user.book_count += 1
            book.borrowed_by = user.name
        return f"A {user.user_type} has borrowed {book.title}."
    
    def return_book(self, book, user):
        book.is_avaliable = True
        book.borrowed_by = None
        user.book_count -= 1
        return f"{book.title} has been returned."
    
    def add_book(self, book, user):
        if user.user_type == "Librarian":
            self.books.append(book)
            return f"{book.title} has been added to the library."
        return f"A {user.user_type} cannot add books to the library."
    
    def remove_book(self, book, user):
        if user.user_type == "Librarian":
            self.books.remove(book)
            return f"{book.title} has been removed from the library."
        return f"A {user.user_type} cannot remove books from the library."
    
    def book_search(self, keyword):
        for book in self.books:
            if keyword in book.title or keyword in book.genre or keyword in book.author:
                return f"{book.title} has been found at the library."
            
        return f"Could not find {keyword}."
    
    def display_status(self):
        for book in self.books:
            if book.is_avaliable:
                print(f"{book.title} is avaliable.")
            else:
                print(f"{book.title} is borrowed by {book.borrowed_by}.")

        return



