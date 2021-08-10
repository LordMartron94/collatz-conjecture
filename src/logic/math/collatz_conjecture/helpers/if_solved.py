from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository


class CheckIfSolved:
    def __init__(self, database, root_number):
        self.database = database
        self.root_number = root_number

    def run(self):
        if CollatzDataRepository(self.database).get_junction_data_by_number(
            self.root_number
        ):
            return True
        return False
