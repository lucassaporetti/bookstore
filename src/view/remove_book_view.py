from pymysql import InternalError

from bookstore.src.core.service.book_service import BookService
from bookstore.src.core.util.tools import print_list, print_warning, print_error, prompt
from bookstore.src.view.menu import Menu

MENU = f"""\033[2J\033[H{'-=' * 15}\n\033[0;34m{'REMOVE A BOOK':^30}\033[0;0;0m\n{'-=' * 15}
\033[0;32m[A]\033[0;0;0m Search a Book
\033[0;32m[B]\033[0;0;0m Delete a Book
\033[0;32m[C]\033[0;0;0m Previous Menu
"""


class RemoveBookView(Menu):
    def __init__(self):
        super().__init__()
        self.menu = MENU
        self.options = ['A', 'B', 'C']
        self.book_service = BookService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            self.search_book()
        elif str_op == 'B':
            self.delete_book()
        elif str_op == 'C':
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

    def search_book(self):
        criteria_hint = '* or criteria_1, ... criteria_N ([book_name|author_name|published|pages|available]=value)'
        criteria = prompt("Please type the search criteria: {}\n$ ".format(criteria_hint), clear=True)
        try:
            if criteria or criteria == '*':
                found = self.book_service.list(filters=criteria if criteria != '*' else None)
                if found and len(found) > 0:
                    print_list(found)
                else:
                    print_warning('No books found for the matching criteria {}'.format(criteria))
        except InternalError:
            print_error('Invalid criteria {}'.format(criteria))

    def delete_book(self):
        entity_id = prompt("Book UUID: ", clear=True)
        if entity_id:
            found = self.book_service.get(entity_id)
            if found is not None:
                self.book_service.delete(entity_id)
            else:
                print_warning('Book with index = {} was not found'.format(entity_id))
