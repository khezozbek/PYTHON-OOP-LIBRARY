class Book:
    def __init__(self, id, title, author, genre):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False

    def return_book(self):
        self.available = True
