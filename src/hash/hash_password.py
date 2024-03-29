import hashlib
from config.config import Config


class HashPassword:

    def __init__(self, salt: str):
        self.salt = salt

    def hash(self, password) -> str:
        password += self.salt

        return hashlib.sha512(password.encode('utf-8')).hexdigest()

    def validate(self, password, hash_token) -> bool:
        return hash_token == self.hash(password)
