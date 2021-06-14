from src.entity.user_meta_data import UserMetaData
from src.storage.database import Database
from src.entity.user import User
from datetime import date


class UserMetaDataRepository:

    def __init__(self, database: Database):
        self.database = database

    def find_all(self) -> list:
        query = """
            SELECT * FROM personal_data
        """

        results = self.database.read_query(query)

        user_meta_data = []
        for data in results:
            user_meta_data.append(self.create_meta_data(data))

        return user_meta_data

    def find_entity_by_id(self, user_id: int) -> UserMetaData:
        query = """
            SELECT * FROM personal_data WHERE userId = %s
        """ % user_id

        result = self.database.read_query(query)

        if not result:
            return None

        return self.create_meta_data(result[0])

    def find_data_id_by_id(self, user_id: int):
        query = """
             SELECT userId FROM personal_data WHERE userId = %s
         """ % user_id

        result = self.database.read_query(query)

        if not result:
            return None

        return result

    def delete(self, user: User):
        # print(user.user_id)
        query = """
            DELETE FROM personal_data 
            WHERE userId = '%s';
        """

        args = (user.user_id,)

        self.database.query(query, args)

    def update(self, user_meta_data: UserMetaData):
        sql = """
             UPDATE personal_data
             SET first_name=%s, last_name=%s, birthday=%s, gender=%s
             WHERE userId = %s;
         """
        args = (user_meta_data.first_name, user_meta_data.last_name, user_meta_data.birthday,
                user_meta_data.gender, user_meta_data.userId)

        self.database.query(sql, args)

    def create(self, first_name: str, last_name: str, birthday: date, gender: str) -> UserMetaData:

        query = """
            INSERT INTO personal_data (first_name, last_name, birthday, gender) 
            VALUES ( %s, %s, %s, %s)
        """

        args = (first_name, last_name, birthday, gender)

        user_meta_data_id = self.database.query(query, args)

        return self.find_entity_by_id(user_meta_data_id)

    @staticmethod
    def create_meta_data(row: list) -> UserMetaData:
        # print(row)
        return UserMetaData(row[0], row[1], row[2], row[3], row[4])
