from src.interfaces.user_exists_interface import UserValidatorInterface

from src.repository.user_repository import UserRepository


class UserExistsByUsername (UserValidatorInterface):
    def __init__(self, database):
        self.database = database
        self.user_repo = UserRepository(self.database)

    def check_by_username(self, username):
        if self.user_repo.get_entity_by_username(username):
            return True
        if not self.user_repo.get_entity_by_username(username):
            return False

