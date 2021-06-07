from src.command.rights_comparison import RightsComparison


class Help:

    def __init__(self, database, logged_in_user):
        self.database = database
        self.logged_in_user = logged_in_user

    @staticmethod
    def show_available_commands():
        # print("Showing commands")
        text = "Here follows a list of all available commands: " + "\n" + "{help | exit | delete user (del) " \
                "| change user type (cut) | Check User Data (cud) | kick user (ku) | ban user (bu)}"
        print(text)
        return

    def check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, 'help').check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self.check_if_allowed():
            # print("Calling commands")
            self.show_available_commands()
            return
        else:
            # print("No way to call!")
            return
