class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.available:
            self.books_borrowed.append(book)
            book.borrow_book()

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.return_book()
