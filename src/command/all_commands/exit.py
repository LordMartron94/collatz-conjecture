from src.command.rights_comparison import RightsComparison


class Exit:

    def __init__(self, database, logged_in_user):
        self.database = database
        self.logged_in_user = logged_in_user

    @staticmethod
    def quit():
        exit()
        return

    def check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, 'exit').check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self.check_if_allowed():
            # print("Calling commands")
            self.quit()
            return
        else:
            # print("No way to call!")
            return
