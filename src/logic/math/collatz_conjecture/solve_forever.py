from src.logic.math.collatz_conjecture.solve import Solve

from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository

import time

wait = time.sleep


class SolveForever:
    def __init__(self, database):
        self.database = database

    def _ask_to_quit(self):
        _quit = input("Do you want to stop solving now? (y/n) ")
        if _quit == "y":
            return True
        elif _quit == "n":
            return False
        else:
            print("Not a valid answer try again! ")
            return self._ask_to_quit()

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

    def _check_if_solved(self, _number):
        if self._check_if_number_exists(_number):
            if self._check_calc_data(_number) == "Already solved":
                return True
            else:
                return False
        else:
            return False

    def run(self):
        n = 4
        num_of_runs = 0

        while True:
            if (num_of_runs % 1000) == 0:
                if self._ask_to_quit():
                    return
                else:
                    pass
            else:
                pass

            if not self._check_if_solved(n):
                if (num_of_runs % 10) == 0:
                    wait(0.5)
                else:
                    pass

                steps_to_solve = Solve(self.database, n).run()
                while len(steps_to_solve) > 0:
                    # print(steps_to_solve)
                    for step in steps_to_solve:
                        Solve(self.database, step).run()
                        steps_to_solve.remove(step)
                else:
                    pass

            else:
                pass

            num_of_runs += 1
            print(f"The current number being solved is: {n}")
            n += 1
