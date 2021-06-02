from src.command.rights_comparison import RightsComparison
from src.repository.user_repository import UserRepository
from src.repository.user_meta_data_repository import UserMetaDataRepository
from src.repository.user_flag_data_repository import UserFlagDataRepository

from src.entity.user import User

from pprint import pprint

import datetime

date = datetime.date


user_repo = UserRepository
user_meta_data_repo = UserMetaDataRepository
user_flag_data_repo = UserFlagDataRepository


class CheckUserData:

    def __init__(self, database, logged_in_user: User):
        self.database = database
        self.logged_in_user = logged_in_user

    def asker(self):
        user_to_see = input('What is the username of the user you want to see the data about? ')
        return user_to_see

    def check_if_allowed(self):
        # print("Check if allowed called!")
        correct = RightsComparison(self.logged_in_user, 'check user data').check_if_allowed()
        return correct

    def retrieve_user_id(self, username):
        _entity = UserRepository(self.database).get_entity_by_username(username)
        _id = _entity.user_id
        return _id

    def check_user_personal_data(self, _user_id):
        user_entity = user_meta_data_repo.find_entity_by_id(user_meta_data_repo(self.database), _user_id)
        _birthday = user_entity.birthday.strftime('%Y-%m-%d')
        data = {'First name': user_entity.first_name, 'Last name': user_entity.last_name,
                'birthday': _birthday, 'gender': user_entity.gender}
        return data

    def check_user_flag_data(self, _user_id):
        user_entity = user_flag_data_repo.find_entity_by_id(user_flag_data_repo(self.database), _user_id)

        isKicked = self.check_bool_value(user_entity.isKicked[0])
        kick_date = self.format_date(user_entity.kick_date)
        remove_kick_date = self.format_date(user_entity.remove_kick_date)
        kick_reason = self.check_if_reason_is_none(user_entity.kick_reason)

        isBanned = self.check_bool_value(user_entity.isBanned[0])
        ban_date = self.format_date(user_entity.ban_date)
        ban_reason = self.check_if_reason_is_none(user_entity.ban_reason)

        data = {'isKicked': isKicked, 'kick_date': kick_date,
                'remove_kick_date': remove_kick_date, 'kick_reason': kick_reason,
                'isBanned': isBanned, 'ban_date': ban_date, 'ban_reason': ban_reason}
        return data

    def check_bool_value(self, _bool):
        if _bool == 0:
            return 'False'
        if _bool == 1:
            return 'True'

    def check_if_reason_is_none(self, reason):
        if type(reason) is str:
            return reason
        if type(reason) is not str:
            return 'None'

    def format_date(self, date_to_format):
        if date_to_format[0]:
            formatted_date = date_to_format[0].strftime('%Y-%m-%d')
            return formatted_date
        if not date_to_format[0]:
            return 'None'

    def run(self):
        # print("Run called")
        if self.check_if_allowed():
            _username = self.asker()
            _id = self.retrieve_user_id(_username)
            personal_data = self.check_user_personal_data(_id)
            flag_data = self.check_user_flag_data(_id)
            print('The personal data of user %s is:' % _username)
            pprint(personal_data, sort_dicts=False)
            print('================================================================')
            print('The flag data of user %s is:' % _username)
            pprint(flag_data, sort_dicts=False)
            return
        else:
            # print("No way to call!")
            return
