from abc import abstractmethod
from bookstore.src.core.factory.factories import SqlFactory
from bookstore.src.core.repository.repository import Repository


class DbRepository(Repository):
    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory.sql_template_file)
        self.sql_factory = sql_factory

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def count(self):
        pass
