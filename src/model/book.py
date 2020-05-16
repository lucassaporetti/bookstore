import uuid

from src.core.enum.color import Color
from src.core.enum.fuel import Fuel
from src.core.enum.yes_no import YesNo
from src.model.entity import Entity


class Car(Entity):
    @staticmethod
    def of(values: list):
        return Car(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])

    def __init__(self, entity_id: str = None, name: str = None, chassis: str = None, color: Color = None,
                 doors: int = None, fuel: Fuel = None, plate: str = None, price: str = None,
                 available: YesNo = YesNo.YES):
        super().__init__(entity_id)
        self.name = name
        self.chassis = chassis
        self.color = color
        self.doors = doors
        self.fuel = fuel
        self.plate = plate
        self.price = price
        self.available = YesNo(available)

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {}".format(
            super().__str__(), self.name, self.chassis, self.color, self.doors, self.fuel, self.plate, self.price,
            self.available)

    class Builder:
        def __init__(self):
            self.uuid = str(uuid.uuid4())
            self.name = None
            self.chassis = None
            self.color = None
            self.doors = 3
            self.fuel = Fuel.FLEX
            self.plate = None
            self.price = None
            self.available = YesNo.YES

        def with_name(self, name: str):
            self.name = name
            return self

        def with_chassis(self, chassis: str):
            self.chassis = chassis
            return self

        def with_color(self, color: Color):
            self.color = color
            return self

        def with_doors(self, doors: int):
            self.doors = doors
            return self

        def with_fuel(self, fuel: Fuel):
            self.fuel = fuel
            return self

        def with_plate(self, plate: str):
            self.plate = plate
            return self

        def with_price(self, price: float):
            self.price = price
            return self

        def with_available(self, available: YesNo):
            self.available = available
            return self

        def build(self):
            return Car(
                self.uuid, self.name, self.chassis, self.color, self.doors, self.fuel, self.plate, self.price,
                self.available
            )
