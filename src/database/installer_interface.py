from src.storage.database import Database


class InstallerInterface:
    def __init__(self, database: Database):
        self.database = database

    def create_table(self):
        """To create a table within the database"""
        pass
