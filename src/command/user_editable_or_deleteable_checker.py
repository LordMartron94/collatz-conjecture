from src.repository import type_repository
from src.repository import user_repository
from src.entity.user import User


class Checker:
    def __init__(self, database, logged_in_user: User):
        self.database = database
        self.logged_in_user = logged_in_user
        self.data = type_repository.TypeRepository().find_all_user_types()

    def get_user_type_edit_data(self, type_to_change_to):
        type_to_change_to_editable_by_list = type_repository.TypeRepository().get_editable_by_type(type_to_change_to)
        return type_to_change_to_editable_by_list

    def get_user_type_delete_data(self, type_to_delete):
        type_to_deletable_by_list = type_repository.TypeRepository().get_deletable_by_type(type_to_delete)
        return type_to_deletable_by_list

    def get_current_user_type(self):
        current_user_type = user_repository.UserRepository(self.database).\
            find_entity_by_username(self.logged_in_user.username).role
        return current_user_type

    def get_user_type(self, user):
        user_type = user_repository.UserRepository(self.database).find_entity_by_username(user).role
        return user_type

    def find_all_changeable_by_user_type(self, user_to_change_type):
        data = self.data
        for Usertype in data:
            # pprint(Usertype, sort_dicts=False)
            # print("---------------------------------------------------")
            if user_to_change_type == Usertype['TypeName']:
                return Usertype['Changeable By To']
        return "Error-message: Usertype not found!"

    def check_changeable_by_user_type(self, user_to_change, type_to_change_to):
        user_logged_in_type = self.get_current_user_type()
        # print("The user logged in type is: %s" % user_logged_in_type)
        user_to_change_type = self.get_user_type(user_to_change)
        # print("The user to change type is: %s" % user_to_change_type)
        change_able_list = self.find_all_changeable_by_user_type(user_to_change_type)
        # print("The changeable list is: %s" % change_able_list)
        # print(type(change_able_list))
        # print(change_able_list)
        # print("======================================================")
        for dictionary in change_able_list:
            # print("The dictionary is: %s" % dictionary)
            # print("------------------------------------")
            # print(type(dictionary))
            for _type, contents in dictionary.items():
                # print(_type, " -> ", contents)
                if user_logged_in_type == _type:
                    for value in contents:
                        if type_to_change_to == value:
                            return True

    def edit_comparison(self, type_to_change_to):
        current_user_type = self.get_current_user_type()
        _edit_list = self.get_user_type_edit_data(type_to_change_to)
        for editable_by_single in _edit_list:
            if editable_by_single == current_user_type:
                return editable_by_single
            return None

    def delete_comparison(self, user_to_delete):
        type_to_delete = self.get_user_type(user_to_delete)
        current_user_type = self.get_current_user_type()
        _delete_list = self.get_user_type_delete_data(type_to_delete)
        for deletable_by_single in _delete_list:
            if deletable_by_single == current_user_type:
                return deletable_by_single
            return None
