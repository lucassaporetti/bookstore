from src.core.service.book_service import BookService
from src.view.builder.book_builder import BookBuilder
from src.view.book_info_ui import BookInfoView
from src.view.car_rental_ui import CarRentalUi
from src.view.listing_ui import ListingUi
from src.view.menu import *
from src.view.user_ui import UserUi

MENU = """\033[2J\033[H
\033[0;32m[0]\033[0;0;0m Exit
\033[0;32m[1]\033[0;0;0m Add Book
\033[0;32m[2]\033[0;0;0m Remove Book
\033[0;32m[3]\033[0;0;0m Edit Book
\033[0;32m[4]\033[0;0;0m List Books
\033[0;32m[5]\033[0;0;0m Search Book
"""


class MainMenuView(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = range(0, 6)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return Menu.EXIT_REQUEST
        elif int_op == 1:
            self.car_service.save(CarBuilder.build())
        elif int_op == 2:
            return UserUi()
        elif int_op == 3:
            return CarRentalUi()
        elif int_op == 4:
            print('Return a Car')
        elif int_op == 5:
            return CarInfoUi()
        elif int_op == 6:
            return ListingUi()

        return Menu.SAME_MENU
