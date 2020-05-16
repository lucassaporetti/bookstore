import pathlib
import sys

from src.core.repository.databases.mysql_repository import MySqlRepository
from src.model.book import Book
from src.model.entity import Entity

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
CAR_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/book_templates.properties"


class BookRepository(MySqlRepository):
    def __init__(self):
        super().__init__(BOOK_TEMPLATES)

    def insert(self, book: Book):
        super().insert(book)

    def update(self, book: Book):
        super().update(book)

    def delete(self, book: Book):
        super().delete(book)