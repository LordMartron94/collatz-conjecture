from src.interfaces.installer_interface import InstallerInterface
from src.storage.database import Database


class UserTableInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("users"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("users"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
            CREATE TABLE users (
            id int PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(40) NOT NULL,
            password VARCHAR(200) NOT NULL,
            role VARCHAR(10) NOT NULL
            );
            """

            self.database.query(query, None)
