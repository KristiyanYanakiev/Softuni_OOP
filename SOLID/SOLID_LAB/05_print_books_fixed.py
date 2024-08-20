class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(content_to_format) -> str:
        return content_to_format + "_formatted"


class Printer:

    @staticmethod
    def get_book(content_to_print) -> str:
        return content_to_print + "_already printed"


formatter = Formatter()
printer = Printer()

book = Book("some_content")

print(formatter.format(book.content))

content_to_format = book.content

formatted = formatter.format(content_to_format)

print(printer.get_book(formatted))




