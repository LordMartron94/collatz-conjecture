import time
from pprint import pprint

from src.logic.math.collatz_conjecture.helpers.if_solved import CheckIfSolved
from src.logic.math.collatz_conjecture.helpers.math import EvenStrategy, CollatzMathStrategy, OddStrategy, CollatzMath
from src.logic.math.collatz_conjecture.helpers.odd_even import OddEven

from src.logic.math.collatz_conjecture.helpers.write_to_db import WriteToDB
from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository
from src.utils.utils import Utilities


def junction_entry_exists(repo, n):
    if repo.check_if_junction_entry_already_exists_by_step(
        n,
        0
    ):
        return True
    return False


class Solve:
    """A class that handles solving one 'main/root' number."""

    def __init__(self, database, root_number: int):
        self.database = database
        self._root_number = root_number

        # Initialize the Repositories
        self.collatz_data_repo = CollatzDataRepository(self.database)
        self.write_to_db = WriteToDB(self.database)

    @staticmethod
    def _choose_strategy(number: int) -> CollatzMathStrategy:
        result = OddEven().run(number)
        if result == "Even":
            return EvenStrategy()
        if result == "Odd":
            return OddStrategy()

    def _add_numbers(self, steps: dict):
        """Generates a new sequence id if the combination doesn't exist yet.
        And also adds the numbers. This method works correctly as intended."""
        sequence_id = self.collatz_data_repo.generate_sequence(self._root_number)

        if sequence_id is not None:
            for step_count, step in steps.items():
                self.write_to_db.add_number(
                    step,
                    step_count,
                    sequence_id
                )

        return None

    def _set_calculation_count(self, steps: dict):
        # pprint(steps)
        calculation_count = (len(steps) - 1)
        self.collatz_data_repo.set_calculation_count(
            self._root_number,
            calculation_count
        )
        return None

    def _set_loop_value(self, steps: dict):
        for step_count, step in steps.items():
            self.collatz_data_repo.set_reached_loop(
                step,
                True
            )

    @staticmethod
    def _side_loop(sequence: list, step_count: int, steps: dict, root_number: int) -> dict:
        for step_tuple in sequence:
            for step in step_tuple:
                if step == root_number:
                    continue

                step_count += 1
                steps[step_count] = step

        return steps

    def _main_loop(self, n, step_count, steps: dict) -> list:
        """Main loop and side loop both work correct."""
        while n != 4:
            if CheckIfSolved(self.database, n).run():
                step_sequence_id = self.collatz_data_repo.get_number_sequence_by_number(n)[0]
                step_sequence = self.collatz_data_repo.get_numbers_by_sequence(step_sequence_id)

                steps = self._side_loop(step_sequence, step_count, steps, n)

                break

            step_count += 1

            strategy = self._choose_strategy(n)
            n = CollatzMath(strategy, n).run()
            steps[step_count] = n

        else:
            pass

        result: list = []

        for step_count, step in steps.items():
            result.append(step)

        return result

    def _edit_result_list(self, result_list: list) -> list:
        """Makes sure numbers are not going to be calculated as a root number again."""

        start = time.time()
        result = result_list

        # print(f"Result v1: {result}")

        for n in result[:]:
            if junction_entry_exists(self.collatz_data_repo, n):  # write this function
                result.remove(n)

        # print(f"Result v2: {result}")

        # exit()
        results = [
            n for n in result
            if n != junction_entry_exists(self.collatz_data_repo, n)
        ]

        end = time.time()
        Utilities.print_time(start, end, "edit the result list")

        return results

    def _end(self, steps: dict):
        self._add_numbers(steps)
        self._set_calculation_count(steps)
        self._set_loop_value(steps)

        return None

    def run(self) -> [list, None]:
        n: int = self._root_number
        step_count: int = 0

        steps: dict = {0: n}

        result = self._main_loop(n, step_count, steps)

        result = self._edit_result_list(result)

        # print(steps)  # Steps are correct here. When solving root number. Not when solving number within sequence...
        # So it goes wrong in either writing to the database, or retrieving the sequence numbers.

        if len(result) > 0:
            """Returns a list of steps to solve as a root number, if the length of the result list is 
            bigger than 0."""

            self._end(steps)

            return result

        else:
            self._end(steps)
            return None

