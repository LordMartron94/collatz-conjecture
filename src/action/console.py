import time

from src.command.function_checker import FunctionChecker
from src.logic.age_updater import AgeUpdater


class Console:

    def __init__(self, database, current_user):
        self.current_user = current_user
        self.database = database

    def run(self):
        # Update user age (to keep it updated)
        # AgeUpdater(self.database, self.current_user).update_age()
        # print(self.current_user.type)
        command_input = input("My Lord, what is your command? ")
        FunctionChecker(self.database, self.current_user, command_input).run()
        time.sleep(1)
        self.run()

