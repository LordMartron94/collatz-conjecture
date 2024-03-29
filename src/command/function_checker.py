from src.command.all_commands import help, exit, test, get_db_size

from src.command.all_commands.User import (
    change_user_type,
    delete_user,
    ban_user,
    check_user_data,
    kick_user,
)

from src.command.all_commands.Math.Collatz import (
    get_sequence,
    solve_specific,
    solve_until,
    solve_forever,
    get_most_steps,
)

from src.repository.User.user_repository import UserRepository


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
            return
        if command.lower() == "ban user" or command.lower() == "bu":
            ban_user.BanUser(
                UserRepository(self.database),
                UserRepository(self.database),
                self.database,
                self.logged_in_user,
            ).run()
            return
        if command.lower() == "test":
            test.Test(self.database, self.logged_in_user).run()
            return
        if command.lower() == "get sequence" or command.lower() == "gs":
            get_sequence.GetSequence(self.database, self.logged_in_user).run()
            return
        if command.lower() == "solve specific" or command.lower() == "ss":
            solve_specific.SolveSpecificNumberCommand(
                self.database, self.logged_in_user
            ).run()
            return
        if command.lower() == "solve until specific" or command.lower() == "sus":
            solve_until.SolveUntilSpecificNumberCommand(
                self.database, self.logged_in_user
            ).run()
            return
        if command.lower() == "solve forever" or command.lower() == "sf":
            solve_forever.SolveForeverCommand(self.database, self.logged_in_user).run()
            return
        if command.lower() == "get most steps" or command.lower() == "gms":
            get_most_steps.GetMostSteps(self.database, self.logged_in_user).run()
            return
        if command.lower() == "get database size" or command.lower() == "gdbs":
            get_db_size.GetDBSize(self.database, self.logged_in_user).run()
            return
        else:
            print("Not a valid command! Try again!")
            return

    def run(self):
        # print(self.logged_in_user)
        self.check_function(self.command)
        return
