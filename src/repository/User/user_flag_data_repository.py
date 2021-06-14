from src.entity.user_flag_data import UserFlagData
from src.storage.database import Database
from src.entity.user import User
from datetime import date


class UserFlagDataRepository:
    def __init__(self, database: Database):
        self.database = database

    def find_all(self) -> list:
        query = """
            SELECT * FROM user_flag_data
        """

        results = self.database.read_query(query)

        user_flag_data = []
        for data in results:
            user_flag_data.append(self._create_meta_data(data))

        return user_flag_data

    def find_entity_by_id(self, user_id: int) -> UserFlagData:
        query = (
            """
            SELECT * FROM user_flag_data WHERE userId = %s
        """
            % user_id
        )

        result = self.database.read_query(query)

        if not result:
            return None

        return self._create_meta_data(result[0])

    def find_data_id_by_id(self, user_id: int):
        query = (
            """
            SELECT userId FROM user_flag_data WHERE userId = %s
        """
            % user_id
        )

        result = self.database.read_query(query)

        if not result:
            return None

        return result

    def delete_by_user_id(self, user: User):
        query = """
            DELETE FROM user_flag_data WHERE userId = '%s';
        """

        args = (user.user_id,)

        self.database.query(query, args)

    def update(self, user_flag_data: UserFlagData):
        sql = """
            UPDATE user_flag_data
            SET isKicked=%s, kick_date=%s, remove_kick_date=%s, kick_reason=%s, isBanned=%s, ban_date=%s,
            ban_reason=%s
            WHERE userId = %s;
       """
        args = (
            user_flag_data.isKicked,
            user_flag_data.kick_date,
            user_flag_data.remove_kick_date,
            user_flag_data.kick_reason,
            user_flag_data.isBanned,
            user_flag_data.ban_date,
            user_flag_data.ban_reason,
            user_flag_data.userId,
        )

        self.database.query(sql, args)

    def create(
        self,
        isKicked: bool,
        kick_date: [date, None],
        remove_kick_date: [date, None],
        kick_reason: [str, None],
        isBanned: bool,
        ban_date: [date, None],
        ban_reason: [str, None],
    ) -> UserFlagData:

        query = """
            INSERT INTO user_flag_data (isKicked, kick_date, remove_kick_date, kick_reason, 
            isBanned, ban_date, ban_reason) 
            VALUES ( %s, %s, %s, %s, %s, %s, %s)
        """

        args = (
            isKicked,
            kick_date,
            remove_kick_date,
            kick_reason,
            isBanned,
            ban_date,
            ban_reason,
        )

        user_meta_data_id = self.database.query(query, args)

        return self.find_entity_by_id(user_meta_data_id)

    @staticmethod
    def _create_meta_data(row: list) -> UserFlagData:
        # print(row)
        return UserFlagData(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )
