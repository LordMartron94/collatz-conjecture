from src.logic.math.collatz_conjecture.solve import Solve


class SolveUntilSpecificNumber:
    def __init__(self, database, number: int):
        self.database = database
        self.number = number

    # TODO: add percentage counter and remove number shower!
    def run(self):
        for number in range(4, (self.number + 1)):
            print(f"The current number being solved is: {number}")
            steps_to_solve = Solve(self.database, number).run()
            while len(steps_to_solve) > 0:
                # print(steps_to_solve)
                for step in steps_to_solve:
                    Solve(self.database, step).run()
                    steps_to_solve.remove(step)
            else:
                pass

        print(f"Numbers 4 until {self.number} have been solved!")
        return
