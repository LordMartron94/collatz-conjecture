from src.command.rights_comparison import RightsComparison
from src.repository.collatz_data_repository import CollatzDataRepository


class Test:
    def __init__(self, database, logged_in_user):
        self.database = database
        self.logged_in_user = logged_in_user

    def functionality(self):
        # dummy_data = [
        #     (4, 0, True, []),
        #     (8, 1, True, [4]),
        #     (16, 2, True, [8, 4]),
        #     (32, 3, True, [16, 8, 4]),
        #     (64, 4, True, [32, 16, 8, 4]),
        # ]
        #
        # for value in dummy_data:
        #     CollatzDataRepository(self.database).insert_new_number(
        #         value[0],  # number
        #         value[1],  # calculation_count
        #         value[2],  # reached_loop
        #         value[3],  # steps
        #

        return

    def check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, "test").check_if_allowed()
        return correct

    def run(self):
        # print("Run called")
        if self.check_if_allowed():
            # print("Calling commands")
            self.functionality()
            return
        else:
            # print("No way to call!")
            return
