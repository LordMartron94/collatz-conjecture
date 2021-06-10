from datetime import date
from dataclasses import dataclass


@dataclass
class UserMetaData:
    userId: int
    first_name: str
    last_name: str
    birthday: date
    gender: str

    def __repr__(self):
        return (
            f"userId: {self.userId}, first_name: {self.first_name}, last_name: {self.last_name}, "
            f"birthday: {self.birthday}, gender: {self.gender}"
        )
