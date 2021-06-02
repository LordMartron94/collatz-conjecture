import time

from src.command.rights_comparison import RightsComparison
from src.repository import user_repository
from src.command import user_editable_or_deleteable_checker

Repo = user_repository.UserRepository
Checker = user_editable_or_deleteable_checker.Checker


wait = time.sleep


class ChangeUserType:

    def __init__(self, database, logged_in_user):
        self.database = database
        self.logged_in_user = logged_in_user
        self.find_logged_in_user_type = Repo(self.database).find_type_by_username(self.logged_in_user)

    @staticmethod
    def ask_user():
        user = input("What is the name of the user you want to change the type of? ")
        return user

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
        Repo(self.database).update_type_by_user_name(user_to_change, type_to_change_to)
        return

    def run(self):
        user_to_change = self.ask_user()
        type_to_change_to = self.ask_type()
        if self.check_if_allowed_to_use_command():
            if self.check_if_allowed_to_change(user_to_change, type_to_change_to):
                self.change(user_to_change, type_to_change_to)
                print("User %s his/her type successfully changed to %s" % (user_to_change, type_to_change_to))
                return
            if not self.check_if_allowed_to_change(user_to_change, type_to_change_to):
                print("You don't have permission to do this!")
                wait(1)
                return
        if not self.check_if_allowed_to_use_command():
            print("You don't have permission to use this command!")
            wait(1)
            return
