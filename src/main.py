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

from src.core.tools import log_init
from src.ui.main_menu_ui import *

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class Main:
    log_file = f"{CUR_DIR}/../log/car-rental.log"
    log = log_init(log_file)
    log.info('Car Rental started {}'.format(datetime.now()))

    def __init__(self):
        self.done = False
        self.ui = MainMenuUi()

    def run(self):
        while not self.done:
            next_ui = self.ui.execute()
            if next_ui is None:
                self.done = True
            elif next_ui == Menu.MAIN_MENU:
                self.ui = MainMenuUi()
            elif next_ui == Menu.SAME_MENU:
                continue
            else:
                self.ui = next_ui


def exit_app(sig=None, frame=None):
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    main = Main()
    signal.signal(signal.SIGINT, exit_app)
    main.run()
    exit_app(0)