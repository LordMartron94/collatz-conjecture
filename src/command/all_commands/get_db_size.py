from src.command.rights_comparison import RightsComparison
from src.interfaces.command_interface import CommandInterface


class GetDBSize(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def get_data(self):
        return self.database.get_database_size()

    def _check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, "gdbs").check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self._check_if_allowed():
            # print("Calling commands")
            print(self.get_data())
            return
        else:
            # print("No way to call!")
            return
