from src.entity.user import User


class UserRepositoryReadInterface:

    def get_all_users(self) -> list:
        pass

    def get_data_by_id(self, user_id: int) -> User:
        pass

    def get_entity_by_username(self, username: str) -> User:
        pass

    def get_user_id_by_username(self, username: str):
        pass


class UserRepositoryWriteInterface:

    def delete(self, user: User):
        pass

    def update(self, user: User):
        pass

    def create(self, username: str, password: str, role: str) -> User:
        pass

    @staticmethod
    def create_user_entity(row: list) -> User:
        pass


