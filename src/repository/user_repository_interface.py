from src.entity.user import User
from src.storage.database import Database


class UserRepositoryReadInterface:

    def find_all(self) -> list:
        pass

    def find_by_id(self, user_id: int) -> User:
        pass

    def find_entity_by_username(self, username: str) -> User:
        pass


class UserRepositoryWriteInterface:

    def save(self):
        pass


