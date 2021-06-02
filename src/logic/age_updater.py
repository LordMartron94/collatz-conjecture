from src.entity.user import User
from src.repository.user_meta_data_repository import UserMetaDataRepository

import datetime

date = datetime.date

user_meta_data_repo = UserMetaDataRepository


class AgeUpdater:
    def __init__(self, database, logged_in_user: User):
        self.database = database
        self.logged_in_user = logged_in_user

    def calculate_age(self):
        meta_data_repo = user_meta_data_repo(self.database)
        user_data = meta_data_repo.find_entity_by_id(self.logged_in_user.user_id)
        birthday = user_data.birthday
        time_difference = date.today() - birthday
        age = int(round(time_difference.days / 365))
        return age

    def update_age(self):
        meta_data_repo = user_meta_data_repo(self.database)
        user_data = meta_data_repo.find_entity_by_id(self.logged_in_user.user_id)
        user_data.age = self.calculate_age()
