from src.entity.user import User
from src.storage.database import Database
from src.interfaces.user_repository_interface import (
    UserRepositoryReadInterface,
    UserRepositoryWriteInterface,
)

from src.repository.user_flag_data_repository import UserFlagDataRepository

from datetime import datetime

date = datetime.date

flag_data_repo = UserFlagDataRepository


class UserRepository(UserRepositoryReadInterface, UserRepositoryWriteInterface):
    def __init__(self, database: Database):
        self.database = database

    def get_all_users(self) -> list:
        query = """
            SELECT * FROM users
        """

        results = self.database.read_query(query)

        users = []
        for data in results:
            users.append(self._create_user_entity(data))

        return users

    def get_data_by_id(self, user_id: int) -> User:
        query = (
            """
            SELECT * FROM users WHERE id = %s
        """
            % user_id
        )

        result = self.database.read_query(query)

        if not result:
            return None

        return self._create_user_entity(result[0])

    def get_entity_by_username(self, username: str) -> User:
        query = (
            """
            SELECT * FROM users WHERE username = '%s'
        """
            % username
        )

        result = self.database.read_query(query)

        if not result:
            return None

        return self._create_user_entity(result[0])

    def get_user_id_by_username(self, username: str):
        query = (
            """
            SELECT id FROM users WHERE username = '%s'
        """
            % username
        )

        result = self.database.fetch_one_in_query(query)

        if not result:
            return None

        return result

    def _get_user_flag_data(self, user: User):
        return flag_data_repo(self.database).find_entity_by_id(user.user_id)

    def get_is_user_kicked(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        val = user_flag_data.isKicked
        if val == 1:
            return True
        else:
            return False

    def get_user_kick_date(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        return user_flag_data.kick_date

    def get_user_kick_reason(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        return user_flag_data.kick_reason

    def get_user_kick_removal_date(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        return user_flag_data.remove_kick_date

    def get_is_user_banned(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        val = user_flag_data.isBanned
        if val == 1:
            return True
        else:
            return False

    def get_user_ban_date(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        return user_flag_data.ban_date

    def get_user_ban_reason(self, user: User):
        user_flag_data = self._get_user_flag_data(user)
        return user_flag_data.ban_reason

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
    def _create_user_entity(row: list) -> User:
        # print(row)
        return User(row[0], row[1], row[2], row[3])

    def set_is_user_kicked(self, user: User, new_value: [bool, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.isKicked = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_user_kick_date(self, user: User, new_value: [date, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.kick_date = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_user_kick_reason(self, user: User, new_value: [str, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.kick_reason = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_user_kick_removal_date(self, user: User, new_value: [date, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.remove_kick_date = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_is_user_banned(self, user: User, new_value: [bool, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.isBanned = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_user_ban_date(self, user: User, new_value: [date, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.ban_date = new_value
        flag_data_repo(self.database).update(user_flag_data)

    def set_user_ban_reason(self, user: User, new_value: [str, None]):
        user_flag_data = self._get_user_flag_data(user)
        user_flag_data.ban_reason = new_value
        flag_data_repo(self.database).update(user_flag_data)
