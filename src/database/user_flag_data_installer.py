from src.database.installer_interface import InstallerInterface
from src.storage.database import Database


class UserFlagDataTableInstaller(InstallerInterface):
    def __init__(self, database: Database):
        super().__init__(database)

    def create_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists("user_flag_data"):
            # print("Table Exists!")
            return

        if not self.database.table_exists("user_flag_data"):
            # print('Creating Table')
            # print("Table does not exist! ")
            query = """
            CREATE TABLE user_flag_data (
            userId int PRIMARY KEY AUTO_INCREMENT,
            isKicked BOOL NOT NULL DEFAULT 0,
            kick_date DATE,
            remove_kick_date DATE,
            kick_reason VARCHAR(400),
            isBanned BOOL NOT NULL DEFAULT 0,
            ban_date DATE,
            ban_reason VARCHAR(400),
            FOREIGN KEY(userId) REFERENCES users(id)
            );
            """

            self.database.query(query, None)
