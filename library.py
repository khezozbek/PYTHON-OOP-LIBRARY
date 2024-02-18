class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.catalog = {}

    def add_book(self, book):
        self.catalog[book.id] = book

    def remove_book(self, book_id):
        del self.catalog[book_id]

    def search_book(self, book_id):
        return self.catalog.get(book_id)

    def display_catalog(self):
        for book_id, book in self.catalog.items():
            print(f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.available}")
