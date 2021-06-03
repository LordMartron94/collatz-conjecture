from src.repository.user_repository import UserRepository
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository
from src.hash.hash_password import HashPassword
from src.file_handling.json import json_storage
from src.logic.user_validator_by_username import UserExistsByUsername

import datetime

date = datetime.date
storage = json_storage.JsonStorage


class Register:
    def __init__(self, repository: UserRepository, meta_data_repo: UserMetaDataRepository,
                 user_flag_data_repo: UserFlagDataRepository, hasher: HashPassword, database):
        self.user_repo = repository
        self.meta_data_repo = meta_data_repo
        self.user_flag_data_repo = user_flag_data_repo
        self.hasher = hasher
        self.json_directory = 'json'
        self.database = database

    def get_user_id(self, _username):
        return self.user_repo.get_user_id_by_username(_username)

    def create_user(self, user_data):
        user = [(str(user_data[0]), str(user_data[1]), 'User')]
        for user in user:
            self.user_repo.create(
                user[0],
                self.hasher.hash(user[1]),
                user[2]
            )

    def create_personal_data(self, user_data):
        user_meta_data = (str(user_data[2]), str(user_data[3]), user_data[4], str(user_data[5]))

        _id = self.get_user_id(user_data[0])

        # print("PERSONAL DATA CALLED")
        if not self.meta_data_repo.find_data_id_by_id(_id):
            # print("NOT!")
            self.meta_data_repo.create(
                user_meta_data[0],  # First Name
                user_meta_data[1],  # Last Name
                user_meta_data[2],  # Birthday
                user_meta_data[3]  # Gender
            )

    def create_user_flag_data(self, user_data):
        flag_data = (False, None, None, None, False, None, None)

        _id = self.get_user_id(user_data[0])

        if not self.user_flag_data_repo.find_data_id_by_id(_id):
            self.user_flag_data_repo.create(
                flag_data[0],  # is kicked
                flag_data[1],  # kick date
                flag_data[2],  # remove kick date
                flag_data[3],  # kick reason
                flag_data[4],  # is banned
                flag_data[5],  # ban date
                flag_data[6]   # ban reason
            )

    def run(self):
        _user_data_collection = GetDataForm(self.user_repo, self.meta_data_repo, self.user_flag_data_repo, self.hasher,
                                            self.database).get_data_form

        _user_data = _user_data_collection()

        self.create_user(_user_data)
        self.create_personal_data(_user_data)
        self.create_user_flag_data(_user_data)


class GetDataForm (Register):
    def __init__(self, repository: UserRepository, meta_data_repo: UserMetaDataRepository,
                 user_flag_data_repo: UserFlagDataRepository, hasher: HashPassword, database):

        super().__init__(repository, meta_data_repo, user_flag_data_repo, hasher, database)

    def get_data_form(self):
        months = storage(self.json_directory).read_json_file_table('months.json', 'Months')

        username = input("What will your username be? ")

        if UserExistsByUsername(self.database).check_by_username(username):
            print("User already exists! Choose a new name!")
            self.get_data_form()
        else:
            pass

        password = input("What will your password be? ")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")

        def validate_year():
            _year = int(input("What is the year you were born? (YYYY) "))

            year_today = datetime.datetime.today().year

            year_list = list(range(year_today, year_today - 120, -1))

            # pprint(year_list)
            # print(type(year_list))
            for YEAR in year_list:
                # print(YEAR)
                if YEAR == _year:
                    return _year
                else:
                    pass
            # exit()

        def validate_month():
            print("NO ABBREVIATIONS!")
            print("Example: June, or February!")
            month_ask = input("What is the month you were born? ")
            for _month in months:
                if _month["Name"].lower() == month_ask.lower():
                    return _month["Id"]

        year = validate_year()
        while year is None:
            if not year:
                print("Invalid year, try again! Date-range: now -120 years.")
                year = validate_year()
        month = validate_month()
        day = int(input("What is the day you were born? (DD) "))
        birthday = date(year, month, day)

        def check_gender():
            _gender = input("What is your gender? a) Male b) Female c) Don't want to tell ")
            if _gender == 'a':
                return 'Male'
            elif _gender == 'b':
                return 'Female'
            elif _gender == 'c':
                return 'Don\'t want to tell'
            else:
                print('This is not a valid gender! Try again!')
                return check_gender()

        gender = check_gender()

        return [username, password, first_name, last_name, birthday, gender]
