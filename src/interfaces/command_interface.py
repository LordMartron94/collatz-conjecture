from src.storage.database import Database

from src.entity.user import User


class CommandInterface:
    def __init__(self, database: Database, logged_in_user: User):
        self.database = database
        self.logged_in_user = logged_in_user

    def _check_if_allowed(self):
        """TO check if the user is allowed to use the command."""

    def run(self):
        """TO run the command."""
