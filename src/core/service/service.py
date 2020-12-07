from abc import ABC
from src.core.repository.repository import Repository
from src.core.util.tools import print_error
from src.model.entity import Entity


class Service(ABC):
    def __init__(self, repository: Repository):
        self.repository = repository

    def save(self, data: Entity):
        if data.uuid is None or self.repository.find_by_id(data.uuid) is None:
            self.repository.insert(data)
        else:
            self.repository.update(data)

    def update(self, data: Entity):
        if Entity:
            self.repository.update(data)
        else:
            print_error('Cannot found that book to edit')

    def delete(self, data: Entity):
        if Entity:
            self.repository.delete(data)
        else:
            print_error('Cannot found that book to delete')

    def list(self, filters: str = None) -> list:
        return self.repository.find_all(filters=filters)

    def get(self, uuid: str) -> Entity:
        return self.repository.find_by_id(uuid)
