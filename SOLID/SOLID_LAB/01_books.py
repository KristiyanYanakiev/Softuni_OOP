from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book_to_library(self, book: Book) -> str:
        self.books.append(book)
        return "book successfully added"

    def find_book(self, title) -> str:

        try:
            book = next(filter(lambda b: b.title == title, self.books))
        except StopIteration:
            return "no such book"
        return f"Here is the searched book with title: {book.title} written by {book.author}"


book1 = Book("test_title", "John")
book2 = Book("second test", "Erick")

my_library = Library()
my_library.add_book_to_library(book1)

print(my_library.find_book("some title"))
print(my_library.find_book("some test_title"))
print(my_library.find_book("test_title"))



