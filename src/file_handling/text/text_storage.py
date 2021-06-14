from time import ctime
import os


class TextStorage:
    def __init__(self, directory):
        self.directory = directory

    def read_text_file(self, file_name):
        try:
            with open(self.directory + "/" + file_name) as text_file:
                return text_file.read()
        except FileNotFoundError:
            print("File was not found!")
        except:
            print("Something else went wrong!")

    def append_text_file(self, data: str, file_name):
        try:
            with open(self.directory + "/" + file_name, "a") as text_file:
                text_file.write(f"{ctime()}  |  {data}\n")
                text_file.close()
        except FileNotFoundError:
            print("File was not found!")
        except Exception as e:
            print(f"Something else went wrong: {e}")

    def delete_text_file(self, file_name):
        os.remove(self.directory + "/" + file_name)
