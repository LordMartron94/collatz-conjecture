from src.entity.user import User
from src.storage.database import Database
from src.interfaces.user_repository_interface import UserRepositoryReadInterface, UserRepositoryWriteInterface


class UserRepository (UserRepositoryReadInterface, UserRepositoryWriteInterface):

    def __init__(self, database: Database):
        self.database = database

    def get_all_users(self) -> list:
        query = """
            SELECT * FROM users
        """

        results = self.database.read_query(query)

        users = []
        for data in results:
            users.append(self.create_user_entity(data))

        return users

    def get_data_by_id(self, user_id: int) -> User:
        query = """
            SELECT * FROM users WHERE id = %s
        """ % user_id

        result = self.database.read_query(query)

        if not result:
            return None

        return self.create_user_entity(result[0])

    def get_entity_by_username(self, username: str) -> User:
        query = """
            SELECT * FROM users WHERE username = '%s'
        """ % username

        result = self.database.read_query(query)

        if not result:
            return None

        return self.create_user_entity(result[0])

    def get_user_id_by_username(self, username: str):
        query = """
            SELECT id FROM users WHERE username = '%s'
        """ % username

        result = self.database.fetch_one_in_query(query)

        if not result:
            return None

        return result

    def delete(self, user: User):
        query = """
            DELETE FROM users WHERE id = %s;
        """

        args = (user.user_id,)

        self.database.query(query, args)

    def update(self, user: User):
        sql = """
            UPDATE users
            SET username=%s, password=%s, role=%s
            WHERE id = %s;
       """
        args = (user.username, user.password, user.role, user.user_id)

        self.database.query(sql, args)

    def create(self, username: str, password: str, role: str) -> User:

        query = """
            INSERT INTO users (username, password, role) 
            VALUES ( %s, %s, %s)
        """

        args = (username, password, role)

        user_id = self.database.query(query, args)

        return self.get_data_by_id(user_id)

    @staticmethod
    def create_user_entity(row: list) -> User:
        # print(row)
        return User(row[0], row[1], row[2], row[3])
