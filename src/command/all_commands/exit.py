from src.command.rights_comparison import RightsComparison
from src.interfaces.command_interface import CommandInterface


class Exit(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    @staticmethod
    def quit():
        exit()
        return

    def _check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, "exit").check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self._check_if_allowed():
            # print("Calling commands")
            self.quit()
            return
        else:
            # print("No way to call!")
            return
