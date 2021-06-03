import time

from src.command.rights_comparison import RightsComparison
from src.repository import user_repository
from src.command import user_editable_or_deleteable_checker
from src.logic.user_validator_by_username import UserExistsByUsername
from src.entity.user import User

Repo = user_repository.UserRepository
Checker = user_editable_or_deleteable_checker.Checker


wait = time.sleep


class ChangeUserType:

    def __init__(self, database, logged_in_user):
        self.database = database
        self.logged_in_user = logged_in_user

    def ask_user(self) -> User:
        username = input("What is the name of the user you want to change the type of? ")
        if UserExistsByUsername(self.database).check_by_username(username):
            return Repo(self.database).get_entity_by_username(username)
        else:
            print("Not a valid username! Try again!")
            wait(1)
            self.ask_user()

    @staticmethod
    def ask_type():
        _type = input("What is the type you want to change the user to? a) Owner, b) Admin, c) Moderator, d) User ")
        if _type == 'a':
            return "Owner"
        if _type == 'b':
            return 'Admin'
        if _type == 'c':
            return 'Moderator'
        if _type == 'd':
            return 'User'
        else:
            print("Not a valid type! Try again!")
            wait(0.5)
            return None

    def check_if_allowed_to_use_command(self):
        correct = RightsComparison(self.logged_in_user, 'change user type').check_if_allowed()
        return correct

    def check_if_allowed_to_change(self, user_to_change, user_type_to_change_to):
        allowed = Checker(self.database, self.logged_in_user).check_changeable_by_user_type(user_to_change,
                                                                                            user_type_to_change_to)
        # print(allowed)
        return allowed

    def change(self, user_to_change, type_to_change_to):
        user_to_change.role = type_to_change_to
        Repo(self.database).update(user_to_change)
        return

    def run(self):
        user_to_change = self.ask_user()
        type_to_change_to = self.ask_type()
        if self.check_if_allowed_to_use_command():
            if self.check_if_allowed_to_change(user_to_change, type_to_change_to):
                self.change(user_to_change, type_to_change_to)
                print("User %s his/her type successfully changed to %s" % (user_to_change.username, type_to_change_to))
                return
            if not self.check_if_allowed_to_change(user_to_change, type_to_change_to):
                print("You don't have permission to do this! Or user is already the type.")
                wait(1)
                return
        if not self.check_if_allowed_to_use_command():
            print("You don't have permission to use this command!")
            wait(1)
            return
