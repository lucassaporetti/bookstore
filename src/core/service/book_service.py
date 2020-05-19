from bookstore.src.core.repository.databases.book_repository import BookRepository
from bookstore.src.core.service.service import Service
from bookstore.src.model.book import Book


class BookService(Service):
    def __init__(self):
        super().__init__(BookRepository())

    def save(self, book: Book):
        super().save(book)

    # def delete(self, book: Book):
    #     super().delete(book)
