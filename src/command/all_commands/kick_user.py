from src.interfaces.user_repository_interface import UserRepositoryWriteInterface
from src.interfaces.user_repository_interface import UserRepositoryReadInterface

from src.entity.user import User

from src.command.rights_comparison import RightsComparison

from src.logic.user_validator_by_username import UserExistsByUsername

from datetime import datetime, timedelta

date = datetime


class KickUser:
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

    def _kick_user(self, user: User, kick_reason):
        self.user_write_repo.set_is_user_kicked(user, True)
        self.user_write_repo.set_user_kick_reason(user, kick_reason)
        self.user_write_repo.set_user_kick_date(user, date.today())

        kick_removal_date = self._calculate_user_kick_removal_date(
            self.user_read_repo.get_user_kick_date(user), self._get_increment()
        )

        self.user_write_repo.set_user_kick_removal_date(user, kick_removal_date)
        self.user_write_repo.set_user_kick_reason(user, kick_reason)

    @staticmethod
    def _get_user_kick_reason(user):
        return input(f"Why do you want to kick user {user.username}? ")

    def _get_increment(self):
        length = input(
            "How long do you want the user to be kicked? a) One week b) Two weeks c) One month, "
            "or d) One year"
        )
        if length == "a":
            return 7
        if length == "b":
            return 14
        if length == "c":
            return 31
        if length == "d":
            return 365
        else:
            print("Not a valid answer! Try again!")
            self._get_increment()

    @staticmethod
    def _calculate_user_kick_removal_date(kick_date: date, increment):
        return kick_date + timedelta(days=increment)

    def _get_user_to_kick(self) -> User:
        username = input("What is the name of the user you want to kick? ")
        if UserExistsByUsername(self.database).check_by_username(username):
            user = self.user_read_repo.get_entity_by_username(username)
            return user
        else:
            print("User does not exist! Try again!")
            self._get_user_to_kick()

    def _check_if_user_is_kickable(self, user_to_kick: User):
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
        if RightsComparison(self.logged_in_user, "kick user").check_if_allowed():
            user_to_kick = self._get_user_to_kick()
            if self._check_if_user_is_kickable(user_to_kick):
                if self._kick_user(
                    user_to_kick, self._get_user_kick_reason(user_to_kick)
                ):
                    print(f"user {user_to_kick} successfully kicked!")
                    return
                else:
                    print("Something went wrong!")
                    return
            else:
                print("Not allowed to kick this user!")
                return
        else:
            print("Not allowed to use this command!")
            return
