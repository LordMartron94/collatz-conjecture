import time

from src.storage.database import Database

from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository

from src.storage.logs import LogManagement


wait = time.sleep


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

    def _check_calc_data(self, number):
        data = CollatzDataRepository(self.database).get_number_by_number(number)
        for value_tuple in data:
            if value_tuple[1] != 0:
                return "Already solved"
            else:
                return "Not yet solved"

    def _check_if_already_solved_as_head(self, number):
        data = CollatzDataRepository(self.database).get_junction_data_by_number(number)
        if data:
            for value_tuple in data:
                if value_tuple[3] == 0:
                    return "Already solved"
                else:
                    return "Not yet solved"
        else:
            return

    def _add_data_to_number(self, _number, _sequence_id, step_count, calculation_count):
        if self._check_calc_data(_number) == "Already solved":
            CollatzDataRepository(self.database).insert_new_junction_entry(
                _number, _sequence_id, step_count
            )
        else:
            CollatzDataRepository(self.database).insert_new_junction_entry(
                _number, _sequence_id, step_count
            )
            CollatzDataRepository(self.database).set_calculation_count(
                _number, calculation_count
            )

    def _insert_new_number(self, _number, _sequence_id, step_count, calculation_count):
        CollatzDataRepository(self.database).insert_new_number(
            _number, calculation_count
        )
        CollatzDataRepository(self.database).insert_new_junction_entry(
            _number, _sequence_id, step_count
        )

    def _add_number(self, _number, _sequence_id, step_count=0, calculation_count=0):
        if self._check_if_number_exists(_number):
            self._add_data_to_number(
                _number, _sequence_id, step_count, calculation_count
            )
        else:
            self._insert_new_number(
                _number, _sequence_id, step_count, calculation_count
            )

    def run(self):
        step_count = 0
        n = int(self.number)
        steps: list = []

        if self._check_if_already_solved_as_head(self.number) == "Already solved":
            return steps

        sequence_id = CollatzDataRepository(self.database).insert_new_sequence()

        while n != 4:
            step_count += 1
            n = self._math(n)
            steps.append(n)
            self._add_number(n, sequence_id, step_count)
        else:
            """Number has reached loop"""
            # print("Number has reached loop!")
            self._add_number(self.number, sequence_id, calculation_count=len(steps))

            CollatzDataRepository(self.database).set_reached_loop(self.number, True)
            for step in steps:
                CollatzDataRepository(self.database).set_reached_loop(step, True)
        LogManagement().write_to_log(steps, "last solved log")
        return steps
