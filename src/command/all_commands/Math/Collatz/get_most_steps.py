from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository

from src.interfaces.command_interface import CommandInterface

from src.command.rights_comparison import RightsComparison


# TODO add number dividers e.g 1.000.000.000 instead of 1000000000
class GetMostSteps(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def _check_if_allowed(self):
        return RightsComparison(self.logged_in_user, "gms")

    def _get_most_steps(self):
        return CollatzDataRepository(self.database).get_calculation()

    def _print_data(self):
        data = self._get_most_steps()
        print(
            f"The number with the most calculation steps solved so far is: {data[0]}, it has {data[1]} steps."
        )

    def run(self):
        if self._check_if_allowed():
            self._print_data()
        else:
            print(
                f"{self.logged_in_user.username} you are not allowed to use this command!"
            )
            return
