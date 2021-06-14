from src.repository.User.user_repository import UserRepository

Repo = UserRepository


class UserValidatorInterface:
    def check_by_username(self, username):
        pass
