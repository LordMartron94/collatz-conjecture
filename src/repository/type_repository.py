from src.file_handling.json.json_storage import *
from pathlib import Path


class TypeRepository:
    def __init__(self):
        self.project_root = str(Path(__file__).resolve().parents[2])
        self.json_directory = 'json'
        self.meta_data_file_name = 'meta_data.json'

    def find_all_user_types(self):
        table = 'UserTypes'
        return JsonStorage(self.json_directory).read_json_file_table(self.meta_data_file_name, table)

    @staticmethod
    def get_type_by_type(_type: str):
        meta_data = TypeRepository().find_all_user_types()
        for key, user_type_meta_data in enumerate(meta_data):
            if _type == user_type_meta_data['TypeName']:
                name = user_type_meta_data['TypeName']
                return name

    def get_meta_data_by_type(self, _type: str):
        meta_data = TypeRepository().find_all_user_types()
        for key, user_type_meta_data in enumerate(meta_data):
            if _type == user_type_meta_data['TypeName']:
                data = user_type_meta_data
                return data

    def get_editable_by_type(self, _type):
        data = self.get_meta_data_by_type(_type)
        editable_by = data['EditableBy']
        return editable_by

    def get_deletable_by_type(self, _type):
        data = self.get_meta_data_by_type(_type)
        deletable_by = data['DeletableBy']
        return deletable_by


