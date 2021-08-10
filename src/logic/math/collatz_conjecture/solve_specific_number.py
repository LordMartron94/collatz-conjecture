import time

from src.logic.math.collatz_conjecture.solve import Solve


class SolveSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    def _print_time(self, start: time.time, end: time.time):
        calculated_time = round(end - start)
        metric = "seconds"

        if calculated_time < 1:
            calculated_time = round((end - start) * 1000)
            metric = "milliseconds"

        print(f"It took {calculated_time} {metric} to solve {self.number}")
        return

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
        self._print_time(start, end)
        return
