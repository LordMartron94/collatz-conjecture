from src.command.all_commands import help
from src.command.all_commands import exit
from src.command.all_commands import delete_user
from src.command.all_commands import change_user_type
from src.command.all_commands import check_user_data
from src.command.all_commands import kick_user
from src.command.all_commands import ban_user

from src.repository.user_repository import UserRepository


class FunctionChecker:
    def __init__(self, database, logged_in_user, command):
        self.command = command
        self.database = database
        self.logged_in_user = logged_in_user

    def check_function(self, command):
        if command.lower() == "help":
            help.Help(self.database, self.logged_in_user).run()
            return
        if command.lower() == "exit" or command.lower() == "quit":
            exit.Exit(self.database, self.logged_in_user).run()
        if command.lower() == "delete user" or command.lower() == "del":
            delete_user.DeleteUser(self.database, self.logged_in_user).run()
            return
        if command.lower() == "change user type" or command.lower() == "cut":
            change_user_type.ChangeUserType(self.database, self.logged_in_user).run()
            return
        if command.lower() == "check user data" or command.lower() == "cud":
            check_user_data.CheckUserData(self.database, self.logged_in_user).run()
            return
        if command.lower() == "kick user" or command.lower() == "ku":
            kick_user.KickUser(
                UserRepository(self.database),
                UserRepository(self.database),
                self.database,
                self.logged_in_user,
            ).run()
        if command.lower() == "ban user" or command.lower() == "bu":
            ban_user.BanUser(
                UserRepository(self.database),
                UserRepository(self.database),
                self.database,
                self.logged_in_user,
            ).run()
        else:
            print("Not a valid command! Try again!")
            return

    def run(self):
        # print(self.logged_in_user)
        self.check_function(self.command)
        return
