from src.command.rights_comparison import RightsComparison
from src.interfaces.command_interface import CommandInterface


class Help(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    @staticmethod
    def show_available_commands():
        # print("Showing commands")
        text = (
            "Here follows a list of all available commands: "
            + "\n"
            + "{help | exit | delete user (del) "
            "| change user type (cut) | Check User Data (cud) | kick user (ku) | ban user (bu) | get sequence (gs) | "
            "solve specific (ss)}"
        )
        print(text)
        return

    def _check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, "help").check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self._check_if_allowed():
            # print("Calling commands")
            self.show_available_commands()
            return
        else:
            # print("No way to call!")
            return
