from src.file_handling.text.text_storage import TextStorage

import os


class LogManagement:
    def __init__(self):
        self.directory = "logs"

    def _check_if_log_exists(self, log):
        path = f"{self.directory}/{log}"
        if os.path.exists(path):
            return True
        else:
            return False

    def write_to_log(self, data: list, log_name: str):
        if self._check_if_log_exists(log_name):
            TextStorage(self.directory).delete_text_file(log_name)
            for line in data:
                TextStorage(self.directory).append_text_file(line, log_name)
            return
        else:
            for line in data:
                TextStorage(self.directory).append_text_file(line, log_name)
            return
