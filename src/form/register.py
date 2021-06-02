from src.repository.user_repository import UserRepository
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository
from src.hash.hash_password import HashPassword
from src.file_handling.json import json_storage
import datetime

date = datetime.date
storage = json_storage.JsonStorage


class Register:
    def __init__(self, repository: UserRepository, meta_data_repo: UserMetaDataRepository,
                 user_flag_data_repo: UserFlagDataRepository, hasher: HashPassword):
        self.user_repo = repository
        self.meta_data_repo = meta_data_repo
        self.user_flag_data_repo = user_flag_data_repo
        self.hasher = hasher
        self.json_directory = 'json'

    def get_user_id(self, _username):
        entity = self.user_repo.get_entity_by_username(_username)
        return entity.user_id

    def get_data_form(self):
        months = storage(self.json_directory).read_json_file_table('months.json', 'Months')

        username = input("What will your username be? ")

        def username_validator():
            if self.get_user_id(username):
                print("This user already exists! Choose a different username!")
                return True
            if not self.get_user_id(username):
                return False

        if username_validator():
            self.get_data_form()
        else:
            pass

        password = input("What will your password be? ")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        year = int(input("What is the year you were born? (YYYY) "))

        def ask_month():
            print("NO ABBREVIATIONS")
            month_ask = input("What is the month you were born? ")
            for month in months:
                if month["Name"].lower() == month_ask.lower():
                    return month["Id"]

        month = ask_month()
        day = int(input("What is the day you were born? (DD) "))

        birthday = date(year, month, day)

        def check_gender():
            gender = input("What is your gender? a) Male b) Female c) Don't want to tell ")
            if gender == 'a':
                return 'Male'
            elif gender == 'b':
                return 'Female'
            elif gender == 'c':
                return 'Don\'t want to tell'
            else:
                print('This is not a valid gender! Try again!')
                return False

        if not check_gender():
            check_gender()
        else:
            gender = check_gender()

        return [username, password, first_name, last_name, birthday, gender]


    # todo: use the form above
    def create_user(self, username, password):
        user = [(str(username), str(password), 'User')]
        for user in user:
            self.user_repo.create(
                user[0],
                self.hasher.hash(user[1]),
                user[2]
            )

    def create_personal_data(self, birthday, first_name, last_name, username):
        user_meta_data = (str(first_name), str(last_name), birthday,
                          str(Register.check_gender()))

        _id = self.get_user_id(username)

        # print("PERSONAL DATA CALLED")
        if not self.meta_data_repo.find_data_id_by_id(_id):
            # print("NOT!")
            self.meta_data_repo.create(
                user_meta_data[0],  # First Name
                user_meta_data[1],  # Last Name
                user_meta_data[2],  # Birthday
                user_meta_data[3]  # Gender
            )

    def create_user_flag_data(self, username):
        flag_data = (False, None, None, None, False, None, None)

        _id = self.get_user_id(username)

        if not self.user_flag_data_repo.find_data_id_by_id(_id):
            self.user_flag_data_repo.create(
                flag_data[0],  # is kicked
                flag_data[1],  # kick date
                flag_data[2],  # remove kick date
                flag_data[3],  # kick reason
                flag_data[4],  # is banned
                flag_data[5],  # ban date
                flag_data[6]  # ban reason
            )

    def run(self):
        username = self.ask_username()

        if not self.check_if_username_already_exists(username):
            password = self.ask_password()
            birthday = self.make_birthday()
            first_name = self.ask_first_name()
            last_name = self.ask_last_name()

            self.create_user(username, password)
            self.create_personal_data(birthday, first_name, last_name, username)
            self.create_user_flag_data(username)
        else:
            self.run()
