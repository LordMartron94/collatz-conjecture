from src.storage.database import Database


class Installer:

    def __init__(self, database: Database):
        self.database = database

    def create_users_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists('users'):
            # print("Table Exists!")
            return

        if not self.database.table_exists('users'):
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

    def create_personal_data_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists('personal_data'):
            # print("Table Exists!")
            return

        if not self.database.table_exists('personal_data'):
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

    def create_user_flag_data_table(self):
        # print("Create Users Table! ")
        if self.database.table_exists('user_flag_data'):
            # print("Table Exists!")
            return

        if not self.database.table_exists('user_flag_data'):
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
