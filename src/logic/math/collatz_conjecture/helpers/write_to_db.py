from src.repository.Math.Collatz.collatz_data_repository import CollatzDataRepository


class WriteToDB:
    def __init__(self, database):
        self.database = database

    def _check_if_number_exists(self, number):
        if CollatzDataRepository(self.database).get_number_by_number(number):
            return True
        else:
            return False

    def _check_calc_data(self, number):
        data = CollatzDataRepository(self.database).get_number_by_number(number)
        for value_tuple in data:
            if value_tuple[1] != 0:
                return "Already solved"
            else:
                return "Not yet solved"

    def _insert_new_junction_entry(self, _number, _sequence_id, step_count):
        if CollatzDataRepository(self.database).check_if_junction_entry_already_exists(_number, step_count):
            # print("Junction already exists! Damn it!")
            return None

        CollatzDataRepository(self.database).insert_new_junction_entry(
            _number, _sequence_id, step_count
        )
        return None

    def _add_data_to_number(self, _number, _sequence_id, step_count):
        self._insert_new_junction_entry(
            _number,
            _sequence_id,
            step_count
        )

        return None

    def _insert_new_number(self, _number, _sequence_id, step_count, calculation_count):
        CollatzDataRepository(self.database).insert_new_number(
            _number, calculation_count
        )
        self._insert_new_junction_entry(
            _number,
            _sequence_id,
            step_count
        )

    def add_number(self, _number: int, step_count: int, _sequence_id: int):
        if self._check_if_number_exists(_number):
            self._add_data_to_number(
                _number, _sequence_id, step_count
            )
        else:
            self._insert_new_number(
                _number, _sequence_id, step_count, 0
            )
