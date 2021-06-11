from src.logic.math.collatz_conjecture.solve import Solve


class SolveSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    def run(self):
        Solve(self.database, self.number).run()
