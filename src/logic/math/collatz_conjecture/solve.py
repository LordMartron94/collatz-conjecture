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

    def _check_if_number_exists(self, number):
        if CollatzDataRepository(self.database).get_number_by_number(number):
            return True
        else:
            return False

    # TODO fix this!
    def run(self):
        step_count = 0
        n = int(self.number)
        steps: list = []
        sequence_id = CollatzDataRepository(self.database).insert_new_sequence()

        while n != 4:
            step_count += 1
            if step_count % 10 == 0:
                time.sleep(0.5)
            else:
                pass
            n = self._math(n)
            steps.append(n)
        else:
            """Number has reached loop"""
            # print("Number has reached loop!")
            if self._check_if_number_exists(self.number):
                CollatzDataRepository(self.database).insert_new_junction_entry(
                    self.number, sequence_id, len(steps)
                )
            else:
                CollatzDataRepository(self.database).insert_new_number(
                    self.number, len(steps), 0, sequence_id
                )
        return steps
