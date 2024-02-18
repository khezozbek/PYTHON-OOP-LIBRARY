# Library Management System

This project is a simple library management system implemented in Python using Object-Oriented Programming (OOP) principles.

## Files

- `library.py`: Contains the `Library` class, which represents a library and its operations such as adding, removing, and searching for books.
- `book.py`: Defines the `Book` class, representing a book with attributes like title, author, genre, and availability status. It also includes methods for borrowing and returning books.
- `member.py`: Defines the `Member` class, representing a library member with attributes like ID, name, and a list of borrowed books. It provides methods for borrowing and returning books.

## Usage

To use the library management system:

1. Import the necessary classes into your Python script or interactive session:

    ```python
    from library import Library
    from book import Book
    from member import Member
    ```

2. Create an instance of the `Library` class:

    ```python
    library = Library("Central Library", "123 Main St")
    ```

3. Create instances of the `Book` class for each book you want to add to the library:

    ```python
    book1 = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction")
    ```

4. Add books to the library using the `add_book()` method:

    ```python
    library.add_book(book1)
    library.add_book(book2)
    ```

5. Create instances of the `Member` class for library members:

    ```python
    member = Member(101, "John")
    ```

6. Allow members to borrow books using the `borrow_book()` method:

    ```python
    member.borrow_book(book1)
    ```

7. Display the library catalog using the `display_catalog()` method:

    ```python
    library.display_catalog()
    ```

## Additional Information.

- Each book has a unique ID assigned to it.
- Members can borrow books if they are available and return them when they're done.
- The library catalog can be displayed to show all available books.

Feel free to expand and customize the functionality as needed for your project.

