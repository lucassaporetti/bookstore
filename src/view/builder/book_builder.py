from bookstore.src.core.util.tools import prompt, print_error
from bookstore.src.core.validator.validators import validate_string, validate_int, validate_date
from bookstore.src.model.book import Book


class BookBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        book = book_name = author_name = published = pages = None
        while not valid:
            book_name = prompt("Book Name: ", clear=True).strip() if book_name is None else book_name
            if not validate_string(book_name, "[a-zA-Z0-9]+", min_len=1, max_len=60):
                print_error(f'Invalid name {book_name}')
                book_name = None
                continue
            author_name = prompt("Author Name: ").strip() if author_name is None else author_name
            if not validate_string(author_name, "[a-zA-Z0-9]+", min_len=1, max_len=60):
                print_error(f'Invalid author name {author_name}')
                author_name = None
                continue
            published = prompt("Published date: ").strip() if published is None else published
            if not validate_date(published, "%d/%m/%Y"):
                print_error(f'Invalid published date {published}')
                published = None
                continue
            pages = prompt("Pages: ").strip() if pages is None else pages
            if not validate_int(pages, min_value=1, max_value=1000):
                print_error(f'Invalid pages number {pages}')
                pages = None
                continue
            valid = True
            book = Book.Builder() \
                .with_author_name(author_name) \
                .with_book_name(book_name) \
                    .with_pages(pages) \
                .with_published(published) \
                .build()

        return book
