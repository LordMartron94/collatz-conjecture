from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository

from src.interfaces.command_interface import CommandInterface

from src.command.rights_comparison import RightsComparison

from src.storage.logs import LogManagement


class GetSequence(CommandInterface):
    def __init__(self, database, logged_in_user):
        super().__init__(database, logged_in_user)

    def _asker(self):
        _number = int(input("What is the number sequence you want to retrieve? "))
        if self._check_if_number_exists(_number):
            return _number
        else:
            print(f"Number: {_number} has not been solved yet.")
            return

    def _check_if_number_exists(self, number):
        if CollatzDataRepository(self.database).get_number_by_number(number):
            return True
        else:
            return False

    def _check_if_allowed(self):
        return RightsComparison(self.logged_in_user, "gs")

    def _get_sequence_data(self, _number):
        return CollatzDataRepository(self.database).get_number_sequence_by_number(
            _number
        )

    def _get_sequence_numbers(self, _id, number_to_find: int):
        sequence_numbers_list = CollatzDataRepository(
            self.database
        ).get_numbers_by_sequence(_id)

        numbers: list = []

        for number_tuple in sequence_numbers_list:
            for number in number_tuple:
                if number == number_to_find:
                    pass
                else:
                    numbers.append(number)

        return numbers

    def _print_data(self, _number):
        sequence_id_tuple = self._get_sequence_data(_number)
        logging_list: list = [_number]

        for _id in sequence_id_tuple:
            numbers = self._get_sequence_numbers(_id, _number)
            print(f"{_number}:")
            for number in numbers:
                print(number)
                logging_list.append(str(number))
        print("\nThis was the sequence!")
        LogManagement().write_to_log(logging_list, "last get_sequence log")

    def run(self):
        if self._check_if_allowed():
            number_to_find = self._asker()
            if number_to_find:
                self._print_data(number_to_find)
            else:
                return
        else:
            print(
                f"{self.logged_in_user.username} you are not allowed to use this command!"
            )
            return
