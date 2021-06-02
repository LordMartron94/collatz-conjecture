import json


class JsonStorage:
    def __init__(self, directory):
        self.json_directory = directory

    def read_json_file(self, file_name):
        # print(file_dir)
        try:
            with open(self.json_directory + '/' + file_name) as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print("File was not found!")
        except:
            print("Something else went wrong!")

    def write_json_file(self, data, file_name):
        try:
            with open(self.json_directory + '/' + file_name, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("File was not found!")
        except:
            print("Something else went wrong!")

    def read_json_file_table(self, file_name, table: str):
        path = self.json_directory
        try:
            return JsonStorage(path).read_json_file(file_name)[table]
        except KeyError:
            print("Table wasn't found!")
        except:
            print("Something else went wrong!")

    def write_json_file_table(self, file_name, table: str, input_data):
        path = self.json_directory
        data = {table: input_data}
        try:
            JsonStorage(path).write_json_file(data, file_name)
        except KeyError:
            print("Table wasn't found!")
        except:
            print("Something else went wrong!")
