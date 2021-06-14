from src.interfaces.command_interface import CommandInterface

from src.command.rights_comparison import RightsComparison

from src.logic.math.collatz_conjecture.solve_forever import (
    SolveForever,
)


class SolveForeverCommand(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def _check_if_allowed(self):
        return RightsComparison(self.logged_in_user, "sf")

    def run(self):
        if self._check_if_allowed():
            SolveForever(self.database).run()
        else:
            print(
                f"{self.logged_in_user.username} you are not allowed to use this command!"
            )
            return
