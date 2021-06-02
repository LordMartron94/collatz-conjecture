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

    def ask_username(self):
        username = input("What will your username be? ")
        return username

    def ask_password(self):
        password = input("What will your password be? ")
        return password

    def ask_first_name(self):
        first_name = input("What is your first name? ")
        return first_name

    def ask_last_name(self):
        last_name = input("What is your last name? ")
        return last_name

    def ask_year(self):
        year = int(input("What is the year you were born? (YYYY) "))
        return year

    def ask_month(self):
        print("NO ABBREVIATIONS")
        month_ask = input("What is the month you were born? ")
        months = storage(self.json_directory).read_json_file_table('months.json', 'Months')
        for month in months:
            if month["Name"].lower() == month_ask.lower():
                return month["Id"]

    def ask_day(self):
        day = int(input("What is the day you were born? (DD) "))
        return day

    def calculate_birthday(self):
        birthday = date(self.ask_year(), self.ask_month(), self.ask_day())
        return birthday

    def check_if_username_already_exists(self, username):
        if self.user_repo.find_user_id_by_username(username):
            print("This user already exists! Choose a different username!")
            return True
        if not self.user_repo.find_user_id_by_username(username):
            return False

    @staticmethod
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
            Register.check_gender()

    def calculate_user_age(self, birthday):
        time_difference = date.today() - birthday
        age = int(round(time_difference.days / 365))
        return age

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

        _id = self.user_repo.find_user_id_by_username(username)

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

        _id = self.user_repo.find_user_id_by_username(username)

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
            birthday = self.calculate_birthday()
            first_name = self.ask_first_name()
            last_name = self.ask_last_name()
            self.create_user(username, password)
            self.create_personal_data(birthday, first_name, last_name, username)
            self.create_user_flag_data(username)
        else:
            self.run()
