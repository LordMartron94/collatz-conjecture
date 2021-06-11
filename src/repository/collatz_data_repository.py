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

    def get_number_by_number(self, number):
        query = """SELECT * FROM collatz_main_data WHERE number=%s""" % number

        results = self.database.read_query(query)

        if not results:
            return None

        return results

    def get_sequences_number_is_in_by_number(self, number: int):
        query = """
            SELECT sequence_id FROM number_to_sequence WHERE number_id = %s;
        """

        args = (number,)
        sequence_ids = self.database.new_query(query, args)

        return sequence_ids

    def get_number_sequence_by_number(self, number: int) -> tuple:
        query = """
                    SELECT sequence_id FROM number_to_sequence WHERE number_id = %s;
                """

        args = (number,)
        sequence_ids = self.database.fetch_one_in_query(query, args)

        return sequence_ids

    def get_numbers_by_sequence(self, sequence_id: int) -> list:
        query = """
                    SELECT number_id FROM number_to_sequence WHERE sequence_id = %s;
                """

        args = (sequence_id,)
        numbers = self.database.new_query(query, args)

        return numbers

    def _insert_new_sequence(self):
        query = """
        INSERT INTO collatz_sequence_data (_null)
        VALUES (%s);
        """

        args = ("None",)

        sequence_id = self.database.query(query, args)

        return sequence_id

    def _insert_new_junction_entry(
        self, number: int, sequence_id: int, step_count: int
    ):
        query = """INSERT INTO number_to_sequence (number_id, sequence_id, step_count)
        VALUES (%s, %s, %s)"""

        args = (number, sequence_id, step_count)

        self.database.query(query, args)

    def insert_new_number(self, number: int, reached_loop: bool, steps: list):

        step_count = 0
        # print(f"original step-count: {step_count}")

        query = """
                    INSERT INTO collatz_main_data (number, calculation_count, reached_loop)
                    VALUES ( %s, %s, %s)
                """

        sequence_id = self._insert_new_sequence()
        calculation_count = len(steps)

        args = (number, calculation_count, reached_loop)

        self.database.query(query, args)

        # print(f"step-count 2: {step_count} should be equal to step-count 1")
        self._insert_new_junction_entry(number, sequence_id, step_count)
        if steps != "[]":
            for _number in steps:
                step_count += 1
                # print(f"step-count 3: {step_count}")
                self._insert_new_junction_entry(_number, sequence_id, step_count)

        return
