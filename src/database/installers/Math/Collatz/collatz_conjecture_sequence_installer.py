from src.storage.database import Database
from src.interfaces.installer_interface import InstallerInterface


class CollatzConjectureSequenceInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("collatz_sequence_data"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("collatz_sequence_data"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
                    CREATE TABLE collatz_sequence_data (
                    sequence_id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    _null VARCHAR(10)
                    );
                    """

            self.database.query(query, None)
