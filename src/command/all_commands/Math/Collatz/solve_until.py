from src.interfaces.command_interface import CommandInterface

from src.command.rights_comparison import RightsComparison

from src.logic.math.collatz_conjecture.solve_until_specific_number import (
    SolveUntilSpecificNumber,
)


class SolveUntilSpecificNumberCommand(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def _asker(self):
        return int(input("What is the number until you want to solve? "))

    def _check_if_allowed(self):
        return RightsComparison(self.logged_in_user, "sus")

    def run(self):
        if self._check_if_allowed():
            number_to_solve = self._asker()
            if number_to_solve:
                SolveUntilSpecificNumber(self.database, number_to_solve).run()
            else:
                return
        else:
            print(
                f"{self.logged_in_user.username} you are not allowed to use this command!"
            )
            return
