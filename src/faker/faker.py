from src.repository.user_repository import UserRepository
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository
from src.hash.hash_password import HashPassword
from datetime import date, timedelta

users = [
    # username, password, type
    ('bernie', 'bernie', 'User'),
    ('ollie', 'ollie', 'User'),
    ('charlie', 'charlie', 'User'),
    ('test_kicked', 'test_kicked', 'User'),
    ('test_banned', 'test_banned', 'User')
]


class Faker:

    def __init__(self, user_repo: UserRepository, meta_data_repo: UserMetaDataRepository,
                 user_flag_data_repo: UserFlagDataRepository, hasher: HashPassword):
        self.user_repo = user_repo
        self.meta_data_repo = meta_data_repo
        self.user_flag_data_repo = user_flag_data_repo
        self.hasher = hasher

    def create_users(self):
        for user in users:
            if not self.user_repo.get_entity_by_username(user[0]):
                self.user_repo.create(
                    user[0],  # username
                    self.hasher.hash(user[1]),  # password
                    user[2],  # role
                )

    def create_personal_data(self):
        date_birthday = date(2002, 5, 17)

        user_meta_data = [
            # each row represents the same row from users (see above)
            # first_name, last_name, age, birthday, gender
            ('Bernie', 'Schutter', date_birthday, 'Female'),
            ('Ollie', 'Schutter', date_birthday, 'Female'),
            ('Charlie', 'Schutter', date_birthday, 'Female'),
            ('Test', 'Kicked', date_birthday, 'Male'),
            ('Test', 'Banned', date_birthday, 'Male')
        ]

        for _id, user in enumerate(users):
            for row in user_meta_data:
                if not self.meta_data_repo.find_entity_by_id(_id):
                    self.meta_data_repo.create(
                        row[0],  # First Name
                        row[1],  # Last Name
                        row[2],  # Birthday
                        row[3]   # Gender
                    )

    def create_user_flag_data(self):
        date_kicked = date.today() + timedelta(days=-3)
        remove_kick_date = date_kicked + timedelta(days=+30)
        date_banned = date.today() + timedelta(days=7)
        user_flag_data = [
            (False, None, None, None, False, None, None),
            (False, None, None, None, False, None, None),
            (False, None, None, None, False, None, None),
            (True, date_kicked, remove_kick_date, 'test kick', False, None, None),
            (False, None, None, None, True, date_banned, 'Reason ban')
        ]

        for _id, user in enumerate(users):
            for row in user_flag_data:
                if not self.user_flag_data_repo.find_entity_by_id(_id):
                    self.user_flag_data_repo.create(
                        row[0],  # is kicked
                        row[1],  # kick date
                        row[2],  # remove kick date
                        row[3],  # kick reason
                        row[4],  # is banned
                        row[5],  # ban date
                        row[6]   # ban reason
                    )
