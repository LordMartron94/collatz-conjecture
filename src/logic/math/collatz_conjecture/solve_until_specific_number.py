import time

from src.logic.math.collatz_conjecture.solve import Solve


class SolveUntilSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    def _print_time(self, start: time.time, end: time.time):
        calculated_time = round(end - start)
        metric = "seconds"

        if calculated_time < 1:
            calculated_time = round((end - start) * 1000)
            metric = "milliseconds"

        print(f"It took {calculated_time} {metric} to solve numbers 4 until {self.number}")
        return

    def run(self):
        start = time.time()
        for number in range(4, (self.number + 1)):
            print(f"The current number being solved is: {number}")
            data = Solve(self.database, number).run()

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
        print(f"Numbers 4 until {self.number} have been solved!")
        self._print_time(start, end)
        return
