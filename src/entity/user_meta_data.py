from datetime import date


class UserMetaData:
    def __init__(self, userId: int, first_name: str, last_name: str, birthday: date, gender: str):
        self.userId = userId
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
