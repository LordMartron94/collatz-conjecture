import time

from src.storage.database import Database
from src.database.installer import Installer
from src.form.authentication_form import AuthenticationForm
from src.repository.user_repository import UserRepository
from src.hash.hash_password import HashPassword
from config.config import Config
from src.faker.faker import Faker
from src.action.console import Console
from mysql.connector import MySQLConnection
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository

config = Config.get_data()

# Database connection
connection = MySQLConnection(
    user=config['db_user'],
    password=config['db_password'],
    host=config['db_host'],
    database=config['db_name']
)
database = Database(connection, config['db_name'])

# Run installer
installer = Installer(database)
installer.create_users_table()
installer.create_personal_data_table()
installer.create_user_flag_data_table()

user_meta_data_repo = UserMetaDataRepository(database)
user_flag_data_repo = UserFlagDataRepository(database)

# User repository
user_repo = UserRepository(database)

# Password hasher
password_hasher = HashPassword(Config.get_data()['AUTH_SALT'])

# Create fake users
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_users()
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_personal_data()
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_user_flag_data()


def login():
    # Authentication form
    login_form = AuthenticationForm(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher, database)

    # Login
    current_user = login_form.run()

    if current_user is not None:
        Console(database, current_user).run()

    if current_user is None:
        time.sleep(1)
        return login()


login()
