from pathlib import Path
from src.file_handling.json.json_storage import JsonStorage


class FunctionsMetaDataRepo:
    def __init__(self):
        self.project_root = str(Path(__file__).resolve().parents[2])
        self.json_directory = 'json'
        self.meta_data_file_name = 'meta_data.json'

    @staticmethod
    def get_names_by_command(command: str):
        meta_data = FunctionsMetaDataRepo().find_all_functions_meta_data()
        for key, function_meta_data in enumerate(meta_data):
            if command == function_meta_data['name'] or command == function_meta_data['alternative_name']:
                names = {function_meta_data['name'], function_meta_data['alternative_name']}
                return names

    @staticmethod
    def get_tooltip_by_command(command: str):
        meta_data = FunctionsMetaDataRepo().find_all_functions_meta_data()
        for key, function_meta_data in enumerate(meta_data):
            if command == function_meta_data['name'] or command == function_meta_data['alternative_name']:
                return function_meta_data['tooltip']

    @staticmethod
    def get_rights_by_command(command: str):
        meta_data = FunctionsMetaDataRepo().find_all_functions_meta_data()
        for key, function_meta_data in enumerate(meta_data):
            if command == function_meta_data['name'] or command == function_meta_data['alternative_name']:
                return function_meta_data['rights']

    def find_all_functions_meta_data(self):
        table = 'Functions'
        return JsonStorage(self.json_directory).read_json_file_table(self.meta_data_file_name, table)

    def print_meta_data(self):
        print(self.json_directory)
