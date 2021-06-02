import time

from src.command.rights_comparison import RightsComparison
from src.repository import user_repository
from src.repository import user_meta_data_repository
from src.repository import user_flag_data_repository
from src.command.user_editable_or_deleteable_checker import Checker
from src.entity.user import User

checker = Checker

UserRepo = user_repository.UserRepository
MetaDataRepo = user_meta_data_repository.UserMetaDataRepository
FlagDataRepo = user_flag_data_repository.UserFlagDataRepository

wait = time.sleep


class DeleteUser:

    def __init__(self, database, logged_in_user: User):
        self.database = database
        self.logged_in_user = logged_in_user

    def delete_user(self, user_to_delete_name):
        user_to_delete = UserRepo(self.database).find_entity_by_username(user_to_delete_name)

        MetaDataRepo(self.database).delete(user_to_delete)
        FlagDataRepo(self.database).delete_by_user_id(user_to_delete)
        UserRepo(self.database).delete(user_to_delete)

        return

    @staticmethod
    def asker():
        user = input("What is the name of the user you want to delete? ")
        return user

    def check_if_allowed_to_use(self):
        correct = RightsComparison(self.logged_in_user, 'delete user').check_if_allowed()
        return correct

    def check_if_allowed_to_delete(self, user_to_delete):
        # print("Check if allowed called!")
        check_user_to_delete_name = UserRepo(self.database).find_entity_by_username(user_to_delete).username
        if check_user_to_delete_name == self.logged_in_user:
            UserRepo(self.database).delete(user_to_delete)
            print("Successfully deleted user %s" % user_to_delete)
            wait(1)
            exit()
        else:
            if checker(self.database, self.logged_in_user).delete_comparison(user_to_delete):
                return True
            if not checker(self.database, self.logged_in_user).delete_comparison(user_to_delete):
                return False
        return False

    def run(self):
        if self.check_if_allowed_to_use():
            user_to_delete = DeleteUser.asker()
            if self.check_if_allowed_to_delete(user_to_delete):
                if self.delete_user(user_to_delete):
                    print("%s, user %s is successfully deleted!" % (self.logged_in_user.username, user_to_delete))
                    wait(1)
                    return
                if not self.delete_user(user_to_delete):
                    print("Something went wrong!")
                    wait(1)
                    exit()
            if not self.check_if_allowed_to_delete(user_to_delete):
                print("%s, you are not allowed to delete %s" % (self.logged_in_user.username, user_to_delete))
        if not self.check_if_allowed_to_use():
            print("%s, you are not allowed to use this command!" % self.logged_in_user.username)
            wait(1)
            return
