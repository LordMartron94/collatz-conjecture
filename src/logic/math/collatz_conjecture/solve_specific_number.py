import time

from src.logic.math.collatz_conjecture.solve import Solve
from src.utils.utils import print_time


class SolveSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    def run(self):
        start = time.time()
        data = Solve(self.database, self.number).run()

        if data is not None:
            steps_to_solve: list = data[:]

            while len(steps_to_solve) > 0:
                # print(steps_to_solve)
                for step in steps_to_solve:
                    Solve(self.database, step).run()
                    steps_to_solve.remove(step)

            else:
                pass

        end = time.time()
        print(f"Number {self.number} has been solved!")
        print_time(start, end, f"solve number {self.number}")
        return
