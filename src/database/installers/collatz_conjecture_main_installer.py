from src.storage.database import Database
from src.interfaces.installer_interface import InstallerInterface


class CollatzConjectureMainInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("collatz_main_data"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("collatz_main_data"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
                    CREATE TABLE collatz_main_data (
                    number int PRIMARY KEY,
                    calculation_count int,
                    reached_loop BOOL DEFAULT 0
                    );
                    """

            self.database.query(query, None)
