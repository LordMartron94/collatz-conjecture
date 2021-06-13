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

    def write_text_file(self, data, file_name):
        try:
            with open(self.directory + "/" + file_name, "w") as text_file:
                text_file.write(data)
        except FileNotFoundError:
            print("File was not found!")
        except:
            print("Something else went wrong!")
