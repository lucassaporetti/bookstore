import pathlib
import sys

from src.core.factory.factories import SqlFactory
from src.core.repository.databases.mysql_repository import MySqlRepository
from src.model.book import Book
from src.model.entity import Entity

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
BOOK_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/book_templates.properties"


class BookRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactory(BOOK_TEMPLATES))

    def insert(self, book: Book):
        super().insert(book)

    def update(self, entity_id):
        super().update(entity_id)

    def delete(self, entity_id):
        super().delete(entity_id)

    def row_to_entity(self, row: tuple) -> Entity:
        return Book.of(list(row))
