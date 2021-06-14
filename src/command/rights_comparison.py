from src.entity.user import User
from src.repository.User.function_meta_data_repository import *


class RightsComparison:
    def __init__(self, user: User, command: str):
        self.user = user
        self.command = command

    def get_function_roles(self):
        return FunctionsMetaDataRepo().get_rights_by_command(self.command)

    def get_user_type(self):
        return self.user.role

    def check_if_allowed(self):
        function_rights = self.get_function_roles()

        user_role = self.user.role

        for role in function_rights:
            if user_role == role:
                # print("Usertype correct, you may proceed!")
                return True
        return False
