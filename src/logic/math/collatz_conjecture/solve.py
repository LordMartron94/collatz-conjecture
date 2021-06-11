import time

from src.storage.database import Database

from src.repository.collatz_data_repository import CollatzDataRepository


class Solve:
    def __init__(self, database: Database, number: int):
        self.database = database
        self.number = number

    def _check_if_number_is_even_or_odd(self, _number):
        if (_number % 2) == 0:
            return "Even"
        else:
            return "Odd"

    def _math(self, _number):
        if self._check_if_number_is_even_or_odd(_number) == "Even":
            return int(_number / 2)
        else:
            return (_number * 3) + 1

    # TODO fix this!
    def run(self):
        step_count = 0
        n = int(self.number)
        steps: list = []

        while n != 4:
            step_count += 1
            steps.append(n)
            if step_count % 10 == 0:
                time.sleep(0.5)
            else:
                pass
            n = self._math(n)
        else:
            """Number has reached loop"""
            print("Number has reached loop!")
            CollatzDataRepository(self.database).insert_new_number(n, True, steps)
            return
