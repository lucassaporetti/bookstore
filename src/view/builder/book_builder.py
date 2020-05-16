from src.core.enum.color import Color
from src.core.enum.fuel import Fuel
from src.core.tools import prompt, print_error
from src.core.validators import validate_string, validate_enum, validate_int, validate_float
from src.model.car import Car


class CarBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        car = name = chassis = color = doors = fuel = plate = price = None
        while not valid:
            name = prompt("Name: ", clear=True).strip() if name is None else name
            if not validate_string(name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
                name = None
                print_error('Invalid name', name)
                continue
            chassis = prompt("Chassis: ").strip() if chassis is None else chassis
            if not validate_string(chassis, "[a-zA-Z0-9]+", min_len=11, max_len=11):
                chassis = None
                print_error('Invalid chassis', chassis)
                continue
            color = prompt("Color: ").strip() if color is None else color
            if not validate_enum(color, Color):
                color = None
                print_error('Invalid color', color)
                continue
            doors = prompt("Doors: ").strip() if doors is None else doors
            if not validate_int(doors, min_value=3, max_value=6):
                doors = None
                print_error('Invalid doors', doors)
                continue
            fuel = prompt("Fuel: ").strip() if fuel is None else fuel
            if not validate_enum(fuel, Fuel):
                fuel = None
                print_error('Invalid fuel', fuel)
                continue
            plate = prompt("Plate: ").strip() if plate is None else plate
            if not validate_string(plate, "[a-zA-Z]{3}-[0-9]{4}", min_len=8, max_len=8):
                plate = None
                print_error('Invalid plate', plate)
                continue
            price = prompt("Price: ").strip() if price is None else price
            if not validate_float(price, min_value=50.0, max_value=1000.0):
                price = None
                print_error('Invalid price', price)
                continue
            valid = True
            car = Car.Builder() \
                .with_name(name) \
                .with_chassis(chassis) \
                .with_color(color) \
                .with_doors(doors) \
                .with_fuel(fuel) \
                .with_plate(plate) \
                .with_price(price) \
                .build()

        return car
