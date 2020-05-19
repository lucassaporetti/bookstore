#!/usr/bin/env python

"""
  @package: TODO describe
   @script: Python 3.7
  @purpose: Bookstore system project to study classes and design patterns
  @created: Sat 16, 2020
   @author: Lucas Saporetti
   @mailto: lucassaporetti@gmail.com
"""

import pathlib
import signal
import sys
from datetime import datetime
from bookstore.src.core.util.tools import log_init
from bookstore.src.view.main_menu_view import *

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class Main:
    log_file = f"{CUR_DIR}/../log/bookstore.log"
    log = log_init(log_file)
    log.info('Bookstore started {}'.format(datetime.now()))

    def __init__(self):
        self.done = False
        self.view = MainMenuView()

    def run(self):
        while not self.done:
            next_view = self.view.execute()
            if next_view is None:
                self.done = True
            elif next_view == Menu.MAIN_MENU:
                self.view = MainMenuView()
            elif next_view == Menu.SAME_MENU:
                continue
            else:
                self.view = next_view


def exit_app(sig=None, frame=None):
    print('\033[2J\033[H')
    print('See you later! ;)')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    main = Main()
    signal.signal(signal.SIGINT, exit_app)
    main.run()
    exit_app(0)
