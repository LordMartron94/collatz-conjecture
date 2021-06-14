from src.interfaces.user_repository_interface import UserRepositoryReadInterface
from src.repository.User.user_meta_data_repository import UserMetaDataRepository
from src.repository.User.user_flag_data_repository import UserFlagDataRepository
from src.entity.user import User
from src.hash.hash_password import HashPassword
from src.form.register import Register

import datetime

date = datetime.date


class AuthenticationForm:
    def __init__(
        self,
        user_repo: UserRepositoryReadInterface,
        meta_data_repo: UserMetaDataRepository,
        user_flag_data_repo: UserFlagDataRepository,
        hasher: HashPassword,
        database,
    ):
        self.user_repo = user_repo
        self.hasher = hasher
        self.meta_data_repo = meta_data_repo
        self.user_flag_data_repo = user_flag_data_repo
        self.database = database

        self.choice = input("Do you want to a) login b) register? ")

    def validate_password(self, user: User, password: str) -> bool:
        return self.hasher.validate(password, user.password)

    def login(self) -> User:
        username = input("What is your username? ")
        password = input("What is your password? ")

        user = self.user_repo.get_entity_by_username(username)

        if not user or not self.validate_password(user, password):
            print("Incorrect user or password! Try again!")
            return None

        def get_kick_removal_str(user_repo, _user):
            return user_repo.get_user_kick_removal_date(_user)

        if self.user_repo.get_is_user_kicked(user):
            kick_remove_date = get_kick_removal_str(self.user_repo, user)
            print(
                f"{user.username} you are kicked, and cannot login until: "
                f"{kick_remove_date}"
            )
            self.login()
        if self.user_repo.get_is_user_banned(user):
            print(f"{user.username}, you are banned and can't ever login again!")
            self.login()

        return user

    def register(self):
        Register(
            self.user_repo,
            self.meta_data_repo,
            self.user_flag_data_repo,
            self.hasher,
            self.database,
        ).run()
        return

    def run(self):
        if self.choice == "a":
            user = self.login()
            return user
        if self.choice == "b":
            self.register()
            print("You can now log in!")
        if self.choice != "a" and self.choice != "b":
            print("This is not a valid option! Try again!")
            return None
