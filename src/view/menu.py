from abc import ABC, abstractmethod

from src.core.util.tools import print_error, prompt


class Menu(ABC):
    EXIT_REQUEST = None
    MAIN_MENU = 0
    SAME_MENU = 1

    def __init__(self):
        self.done = False
        self.op = None
        self.menu = ''
        self.options = []

    def execute(self):
        while not self.op == Menu.MAIN_MENU and not self.done:
            print(self.menu)
            self.op = prompt("$ ", end='')
            if self.op.isalnum() and self.op_in_options():
                return self.trigger_menu_item()
            else:
                print_error("Invalid option '{}'".format(self.op))

    @abstractmethod
    def trigger_menu_item(self):
        pass

    def op_in_options(self):
        if self.op.isdigit():
            return int(self.op) in self.options
        else:
            return False
