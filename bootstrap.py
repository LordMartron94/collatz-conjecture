import time

from src.storage.database import Database
from src.database.installers.user_table_installer import UserTableInstaller
from src.database.installers.user_flag_data_installer import UserFlagDataTableInstaller
from src.database.installers.user_meta_data_installer import UserMetaDataTableInstaller
from src.database.installers.collatz_conjecture_main_installer import (
    CollatzConjectureMainInstaller,
)
from src.database.installers.collatz_conjecture_sequence_installer import (
    CollatzConjectureSequenceInstaller,
)
from src.database.installers.collatz_conjecture_junction_installer import (
    CollatzConjectureJunctionInstaller,
)
from src.form.authentication_form import AuthenticationForm
from src.repository.user_repository import UserRepository
from src.hash.hash_password import HashPassword
from config.config import Config
from src.action.console import Console
from mysql.connector import MySQLConnection
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository

config = Config.get_data()

# Database connection
connection = MySQLConnection(
    user=config["db_user"],
    password=config["db_password"],
    host=config["db_host"],
    database=config["db_name"],
)
database = Database(connection, config["db_name"])

# Run installers
UserTableInstaller(database).create_table()
UserMetaDataTableInstaller(database).create_table()
UserFlagDataTableInstaller(database).create_table()

CollatzConjectureSequenceInstaller(database).create_table()
CollatzConjectureMainInstaller(database).create_table()
CollatzConjectureJunctionInstaller(database).create_table()

user_meta_data_repo = UserMetaDataRepository(database)
user_flag_data_repo = UserFlagDataRepository(database)

# User repository
user_repo = UserRepository(database)

# Password hasher
password_hasher = HashPassword(Config.get_data()["AUTH_SALT"])

# Create fake users
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_users()
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_personal_data()
# Faker(user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher).create_user_flag_data()


def login():
    # Authentication form
    login_form = AuthenticationForm(
        user_repo, user_meta_data_repo, user_flag_data_repo, password_hasher, database
    )

    # Login
    current_user = login_form.run()

    if current_user is not None:
        Console(database, current_user).run()

    if current_user is None:
        time.sleep(1)
        return login()


login()
