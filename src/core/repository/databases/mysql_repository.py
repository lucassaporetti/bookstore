import pathlib
import sys
import uuid
from abc import abstractmethod
from typing import Optional
import pymysql
from pymysql import ProgrammingError, OperationalError
from bookstore.src.core.factory.factories import SqlFactory
from bookstore.src.core.property.properties import Properties
from bookstore.src.core.repository.databases.db_repository import DbRepository
from bookstore.src.core.util.tools import log_init, print_error
from bookstore.src.main import Main
from bookstore.src.model.entity import Entity

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
DB_PROPERTIES = Properties(f"{CUR_DIR}/db.properties").read()
LOG = log_init(Main.log_file)


class MySqlRepository(DbRepository):
    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory)
        self.hostname = DB_PROPERTIES.get('db.hostname')
        self.port = DB_PROPERTIES.get_int('db.port')
        self.user = DB_PROPERTIES.get('db.user')
        self.password = DB_PROPERTIES.get('db.password')
        self.database = DB_PROPERTIES.get('db.database')
        self.connector = None
        self.cursor = None
        self.connect()

    def __str__(self):
        return "{}@{}:{}/{}".format(self.user, self.hostname, self.port, self.database)

    def is_connected(self):
        return self.connector is not None

    def connect(self):
        if not self.is_connected():
            try:
                self.connector = pymysql.connect(
                    host=self.hostname,
                    user=self.user,
                    port=self.port,
                    password=self.password,
                    database=self.database
                )
                assert self.is_connected(), "Not connected to the database"
                self.cursor = self.connector.cursor()
                LOG.info('Connected to {} established'.format(str(self)))
            except OperationalError:
                LOG.error('Unable to connect to {}'.format(str(self)))
                print_error('Unable to connect to {}'.format(str(self)))
                sys.exit(1)

        return self.connector

    def disconnect(self):
        if self.is_connected():
            self.connector.close()
            self.connector = None
            LOG.info('Disconnected from {}.'.format(str(self)))
        else:
            LOG.error('Unable to disconnect from {}'.format(str(self)))
            sys.exit(1)

        return self.connector

    def count(self):
        count_stm = self.sql_factory.count()
        LOG.info('Executing SQL statement: {}'.format(count_stm))
        self.cursor.execute(count_stm)
        ret_val = self.cursor.fetchall()

        return ret_val

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else str(uuid.uuid4())
        insert_stm = self.sql_factory.insert(entity.__dict__)
        LOG.info('Executing SQL statement: {}'.format(insert_stm))
        self.cursor.execute(insert_stm)
        self.connector.commit()

    def update(self, entity: Entity):
        update_stm = self.sql_factory.update(entity.__dict__, filters=[
            'UUID = {}'.format(entity.uuid)
        ])
        LOG.info('Executing SQL statement: {}'.format(update_stm))
        self.cursor.execute(update_stm)
        self.connector.commit()

    def delete(self, entity_id: str):
        if entity_id:
            delete_stm = self.sql_factory.delete(filters=[
                "UUID = '{}'".format(entity_id)
            ])
            LOG.info('Executing SQL statement: {}'.format(delete_stm))
            self.cursor.execute(delete_stm)
            self.connector.commit()
            print(f'Book with index {entity_id} successfully deleted from the database')
        else:
            print_error('Cannot delete this book from database')

    def find_all(self, filters: str = None) -> Optional[list]:
        if filters is not None:
            sql_filters = filters.upper().replace(',', ', OR ').split(',')
        else:
            sql_filters = None
        select_stm = self.sql_factory.select(filters=sql_filters)
        LOG.info('Executing SQL statement: {}'.format(select_stm))
        try:
            self.cursor.execute(select_stm)
            result = self.cursor.fetchall()
            ret_val = []
            for next_row in result:
                ret_val.append(self.row_to_entity(next_row))
            return ret_val
        except ProgrammingError:
            return None

    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        if entity_id:
            select_stm = self.sql_factory.select(filters=[
                "UUID = '{}'".format(entity_id)
            ])
            LOG.info('Executing SQL statement: {}'.format(select_stm))
            self.cursor.execute(select_stm)
            result = self.cursor.fetchall()
            return result[0] if len(result) > 0 else None
        else:
            return None

    @abstractmethod
    def row_to_entity(self, row: tuple) -> Entity:
        pass
