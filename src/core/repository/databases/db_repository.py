from abc import abstractmethod
from src.core.repository.repository import Repository


class DbRepository(Repository):
    def __init__(self):
        super().__init__()

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
