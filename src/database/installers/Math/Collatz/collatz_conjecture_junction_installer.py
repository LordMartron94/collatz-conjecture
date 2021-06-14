from src.storage.database import Database
from src.interfaces.installer_interface import InstallerInterface


class CollatzConjectureJunctionInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("number_to_sequence"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("number_to_sequence"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
                    CREATE TABLE number_to_sequence (
                    junction_id int PRIMARY KEY AUTO_INCREMENT,
                    number_id BIGINT,
                    sequence_id BIGINT,
                    step_count BIGINT,
                    FOREIGN KEY(number_id) REFERENCES collatz_main_data(number),
                    FOREIGN KEY(sequence_id) REFERENCES collatz_sequence_data(sequence_id),
                    CONSTRAINT uc_number_sequence UNIQUE (number_id, sequence_id)
                    );
                    """

            self.database.query(query, None)
