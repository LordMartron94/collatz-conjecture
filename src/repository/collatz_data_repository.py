from src.storage.database import Database


class CollatzDataRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_all_numbers(self) -> list:
        query = """
            SELECT * FROM collatz_main_data
        """

        results = self.database.read_query(query)

        return results

    def get_sequences_number_is_in_by_number(self, number: int):
        query = """
            SELECT sequence_id FROM number_to_sequence WHERE number_id = %s;
        """

        args = (number,)
        sequence_ids = self.database.new_query(query, args)

        return sequence_ids

    def get_number_sequence_by_number(self, number: int):
        # TODO make this!
        pass

    def _insert_new_sequence(self):
        query = """
        INSERT INTO collatz_sequence_data (_null)
        VALUES (%s);
        """

        args = ("None",)

        sequence_id = self.database.query(query, args)

        return sequence_id

    def _insert_new_junction_entry(self, number, sequence_id):
        query = """INSERT INTO number_to_sequence (number_id, sequence_id)
        VALUES (%s, %s)"""

        args = (number, sequence_id)

        self.database.query(query, args)

    def insert_new_number(
        self, number: int, calculation_count: int, reached_loop: bool, steps: list
    ):
        query = """
                    INSERT INTO collatz_main_data (number, calculation_count, reached_loop) 
                    VALUES ( %s, %s, %s)
                """

        sequence_id = self._insert_new_sequence()

        args = (number, calculation_count, reached_loop)

        self.database.query(query, args)

        if steps != "[]":
            for _number in steps:
                self._insert_new_junction_entry(_number, sequence_id)
        self._insert_new_junction_entry(number, sequence_id)

        return
