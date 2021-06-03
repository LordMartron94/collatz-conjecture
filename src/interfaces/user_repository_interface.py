from src.entity.user import User
from datetime import datetime

date = datetime.date


class UserRepositoryReadInterface:

    def get_all_users(self) -> list:
        pass

    def get_data_by_id(self, user_id: int) -> User:
        pass

    def get_entity_by_username(self, username: str) -> User:
        pass

    def get_user_id_by_username(self, username: str):
        pass

    def get_is_user_kicked(self, user: User):
        pass

    def get_user_kick_date(self, user: User):
        pass

    def get_user_kick_reason(self, user: User):
        pass

    def get_user_kick_removal_date(self, user: User):
        pass

    def get_is_user_banned(self, user: User):
        pass

    def get_user_ban_date(self, user: User):
        pass

    def get_user_ban_reason(self, user: User):
        pass


class UserRepositoryWriteInterface:

    def delete(self, user: User):
        pass

    def update(self, user: User):
        pass

    def create(self, username: str, password: str, role: str) -> User:
        pass

    def set_is_user_kicked(self, user: User, new_value: [bool, None]):
        pass

    def set_user_kick_date(self, user: User, new_value: [date, None]):
        pass

    def set_user_kick_reason(self, user: User, new_value: [str, None]):
        pass

    def set_user_kick_removal_date(self, user: User, new_value: [date, None]):
        pass

    def set_is_user_banned(self, user: User, new_value: [bool, None]):
        pass

    def set_user_ban_date(self, user: User, new_value: [date, None]):
        pass

    def set_user_ban_reason(self, user: User, new_value: [str, None]):
        pass

