from library import Library
from book import Book
from member import Member

library = Library("Central Library", "123 Main St")
book1 = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction")
library.add_book(book1)
library.add_book(book2)

member = Member(101, "John")
member.borrow_book(book1)

library.display_catalog()
