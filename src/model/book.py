import uuid
from bookstore.src.core.enum.yes_no import YesNo
from bookstore.src.model.entity import Entity


class Book(Entity):
    @staticmethod
    def of(values: list):
        return Book(values[0], values[1], values[2], values[3], values[4])

    def __init__(self, entity_id: str = None, book_name: str = None, author_name: str = None, published: str = None,
                 pages: int = None, available: YesNo = YesNo.YES):
        super().__init__(entity_id)
        self.book_name = book_name
        self.author_name = author_name
        self.published = published
        self.pages = pages
        self.available = YesNo(available)

    def __str__(self):
        return "{} | {} | {} | {} | {} | {}".format(
            super().__str__(), self.book_name, self.author_name, self.published, self.pages, self.available)

    class Builder:
        def __init__(self):
            self.uuid = str(uuid.uuid4())
            self.book_name = None
            self.author_name = None
            self.published = None
            self.pages = 1
            self.available = YesNo.YES

        def with_book_name(self, book_name: str):
            self.book_name = book_name
            return self

        def with_author_name(self, author_name: str):
            self.author_name = author_name
            return self

        def with_published(self, published: str):
            self.published = published
            return self

        def with_pages(self, pages: int):
            self.pages = pages
            return self

        def with_available(self, available: YesNo):
            self.available = available
            return self

        def build(self):
            return Book(
                self.uuid, self.book_name, self.author_name, self.published, self.pages, self.available
            )
