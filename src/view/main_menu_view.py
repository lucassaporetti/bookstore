from src.core.service.book_service import BookService
from src.core.util.tools import print_list
from src.view.builder.book_builder import BookBuilder
from src.view.edit_book_view import EditBookView
from src.view.menu import *
from src.view.remove_book_view import RemoveBookView
from src.view.search_book_view import SearchBookView

MENU = f"""\033[2J\033[H{'-=' * 15}\n\033[0;34m{'BOOKSTORE':^30}\033[0;0;0m\n{'-=' * 15}
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
        self.menu = MENU
        self.options = range(0, 6)
        self.book_service = BookService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return Menu.EXIT_REQUEST
        elif int_op == 1:
            self.book_service.save(BookBuilder.build())
        elif int_op == 2:
            return RemoveBookView()
        elif int_op == 3:
            return EditBookView()
        elif int_op == 4:
            print_list(self.book_service.list())
        elif int_op == 5:
            return SearchBookView()

        return Menu.SAME_MENU
