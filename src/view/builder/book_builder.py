from bookstore.src.core.util.tools import prompt, print_error
from bookstore.src.core.validator.validators import validate_string, validate_int, validate_date
from bookstore.src.model.book import Book


class BookBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        book = book_name = author_name = published = pages =  None
        while not valid:
            book_name = prompt("Book Name: ", clear=True).strip() if book_name is None else book_name
            if not validate_string(book_name, "[a-zA-Z0-9]+", min_len=1, max_len=60):
                book_name = None
                print_error('Invalid book name', book_name)
                continue
            author_name = prompt("Author: ").strip() if author_name is None else author_name
            if not validate_string(author_name, "[a-zA-Z0-9]+", min_len=1, max_len=60):
                author_name = None
                print_error('Invalid author name', author_name)
                continue
            published = prompt("Published: ").strip() if published is None else published
            if not validate_date(published, "%d/%m/%Y"):
                published = print_error("Invalid published date", published)
                continue
            pages = prompt("Pages: ").strip() if pages is None else pages
            if not validate_int(pages, min_value=1, max_value=1000):
                pages = None
                print_error('Invalid pages number', pages)
                continue
            valid = True
            book = Book.Builder() \
                .with_book_name(book_name) \
                .with_author_name(author_name) \
                .with_published(published) \
                .with_pages(pages) \
                .build()

        return book
