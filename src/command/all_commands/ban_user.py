from src.interfaces.user_repository_interface import UserRepositoryWriteInterface
from src.interfaces.user_repository_interface import UserRepositoryReadInterface

from src.entity.user import User

from src.command.rights_comparison import RightsComparison

from src.logic.user_validator_by_username import UserExistsByUsername

from datetime import datetime, timedelta

date = datetime


class BanUser:
    def __init__(
        self,
        user_write_repo: UserRepositoryWriteInterface,
        user_read_repo: UserRepositoryReadInterface,
        database,
        logged_in_user: User,
    ):
        self.user_write_repo = user_write_repo
        self.user_read_repo = user_read_repo
        self.logged_in_user = logged_in_user
        self.database = database

    def _ban_user(self, user: User, ban_reason):
        self.user_write_repo.set_is_user_banned(user, True)
        self.user_write_repo.set_user_ban_reason(user, ban_reason)
        self.user_write_repo.set_user_ban_date(user, date.today())

        return True

    @staticmethod
    def _get_user_ban_reason(user):
        return input(f"Why do you want to ban user {user.username}? ")

    def _get_user_to_ban(self) -> User:
        username = input("What is the name of the user you want to ban? ")
        if UserExistsByUsername(self.database).check_by_username(username):
            user = self.user_read_repo.get_entity_by_username(username)
            return user
        else:
            print("User does not exist! Try again!")
            self._get_user_to_ban()

    def _check_if_user_is_ban_able(self, user_to_kick: User):
        if self.logged_in_user.role == "Owner":
            return True
        if self.logged_in_user.role == "Admin":
            if user_to_kick.role != "Owner" and "Admin":
                return True
            else:
                return False
        if self.logged_in_user.role == "Moderator":
            if user_to_kick.role == "User":
                return True
            else:
                return False

    def run(self):
        if RightsComparison(self.logged_in_user, "ban user").check_if_allowed():
            user_to_ban = self._get_user_to_ban()
            if self._check_if_user_is_ban_able(user_to_ban):
                if self._ban_user(user_to_ban, self._get_user_ban_reason(user_to_ban)):
                    print(f"user {user_to_ban.username} successfully banned!")
                    return
                else:
                    print("Something went wrong!")
                    return
            else:
                print("Not allowed to ban this user!")
                return
        else:
            print("Not allowed to use this command!")
            return
