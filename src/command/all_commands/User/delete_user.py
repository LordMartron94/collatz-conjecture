import time

from src.command.rights_comparison import RightsComparison
from src.repository.User import (
    user_meta_data_repository,
    user_repository,
    user_flag_data_repository,
)
from src.command.user_editable_or_deleteable_checker import Checker
from src.entity.user import User
from src.logic.user_validator_by_username import UserExistsByUsername

from src.interfaces.command_interface import CommandInterface

checker = Checker

UserRepo = user_repository.UserRepository
MetaDataRepo = user_meta_data_repository.UserMetaDataRepository
FlagDataRepo = user_flag_data_repository.UserFlagDataRepository

wait = time.sleep


class DeleteUser(CommandInterface):
    def __init__(self, database, logged_in_user: User):
        super().__init__(database, logged_in_user)

    def delete_user(self, user_to_delete):
        try:
            MetaDataRepo(self.database).delete(user_to_delete)
            FlagDataRepo(self.database).delete_by_user_id(user_to_delete)
            UserRepo(self.database).delete(user_to_delete)

            return True
        except:
            return False

    def _asker(self):
        username = input("What is the name of the user you want to delete? ")
        if UserExistsByUsername(self.database).check_by_username(username):
            user = UserRepo(self.database).get_entity_by_username(username)
            return user
        if not UserExistsByUsername(self.database).check_by_username(username):
            print("User doesn't exist! Try again!")
            wait(1)
            return self._asker()

    def _check_if_allowed_to_use(self):
        return RightsComparison(self.logged_in_user, "delete user").check_if_allowed()

    def _check_if_allowed_to_delete(self, user_to_delete: User):
        # print("Check if allowed called!")
        if user_to_delete.username == self.logged_in_user.username:
            UserRepo(self.database).delete(user_to_delete)
            print("Successfully deleted user %s" % user_to_delete.username)
            wait(1)
            exit()
        else:
            return checker(self.database, self.logged_in_user).delete_comparison(
                user_to_delete
            )
        return False

    def run(self):
        if self._check_if_allowed_to_use():
            user_to_delete = self._asker()
            if self._check_if_allowed_to_delete(user_to_delete):
                if self.delete_user(user_to_delete):
                    print(
                        "%s, user %s is successfully deleted!"
                        % (self.logged_in_user.username, user_to_delete.username)
                    )
                    wait(1)
                    return
                if not self.delete_user(user_to_delete):
                    print("Something went wrong!")
                    wait(1)
                    exit()
            if not self._check_if_allowed_to_delete(user_to_delete):
                print(
                    "%s, you are not allowed to delete %s"
                    % (self.logged_in_user.username, user_to_delete.username)
                )
        if not self._check_if_allowed_to_use():
            print(
                "%s, you are not allowed to use this command!"
                % self.logged_in_user.username
            )
            wait(1)
            return
