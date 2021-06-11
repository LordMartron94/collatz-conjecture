from src.logic.math.collatz_conjecture.solve import Solve


class SolveSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    def run(self):
        steps_to_solve = Solve(self.database, self.number).run()
        while len(steps_to_solve) > 0:
            for step in steps_to_solve:
                Solve(self.database, step).run()
        else:
            print("Number has reached loop!")
            return
