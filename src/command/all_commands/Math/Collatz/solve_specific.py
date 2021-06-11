from src.repository.collatz_data_repository import CollatzDataRepository

from src.interfaces.command_interface import CommandInterface

from src.command.rights_comparison import RightsComparison

from src.logic.math.collatz_conjecture.solve_specific_number import SolveSpecificNumber


class SolveSpecificNumberCommand(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def _asker(self):
        _number = int(input("What is the number sequence you want to solve? "))
        if self._check_if_number_exists(_number):
            print(f"Number: {_number} has already been solved! Try another one!")
            return None
        else:
            return _number

    def _check_if_number_exists(self, number):
        if CollatzDataRepository(self.database).get_number_by_number(number):
            return True
        else:
            return False

    def _check_if_allowed(self):
        return RightsComparison(self.logged_in_user, "gs")

    def run(self):
        if self._check_if_allowed():
            number_to_solve = self._asker()
            if number_to_solve:
                SolveSpecificNumber(self.database, number_to_solve).run()
            else:
                return
        else:
            print(
                f"{self.logged_in_user.username} you are not allowed to use this command!"
            )
            return
