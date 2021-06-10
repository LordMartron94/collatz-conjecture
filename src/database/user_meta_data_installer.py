from src.database.installer_interface import InstallerInterface
from src.storage.database import Database


class UserMetaDataTableInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("personal_data"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("personal_data"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
            CREATE TABLE personal_data (
            userId int PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            birthday DATE,
            gender VARCHAR(20) NOT NULL DEFAULT 'N/A',
            FOREIGN KEY(userId) REFERENCES users(id)
            );
            """

            self.database.query(query, None)
