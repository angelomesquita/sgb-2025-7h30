import os
from typing import Dict


class View:

    __INVALID_OPTION = 'Invalid option.'

    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def press_enter_to_continue() -> None:
        input('Press <Enter> to continue...')

    @staticmethod
    def run_action(menu_actions: Dict, option: str) -> bool:
        action = menu_actions.get(option)
        if not action:
            print(View.__INVALID_OPTION)
            View.press_enter_to_continue()
            return True
        result = action()
        return result != 'exit'
