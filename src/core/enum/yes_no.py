from enum import Enum


class YesNo(Enum):
    NO = 0
    YES = 1

    def __str__(self):
        return "{}".format(self.value)
