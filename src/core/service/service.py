from abc import ABC
from bookstore.src.core.repository.repository import Repository
from bookstore.src.model.entity import Entity


class Service(ABC):
    def __init__(self, repository: Repository):
        self.repository = repository

    def save(self, data: Entity):
        if data.uuid is None or self.repository.find_by_id(data.uuid) is None:
            self.repository.insert(data)
        else:
            self.repository.update(data)

    def list(self, filters: str = None) -> list:
        return self.repository.find_all(filters=filters)

    def get(self, uuid: str) -> Entity:
        return self.repository.find_by_id(uuid)
