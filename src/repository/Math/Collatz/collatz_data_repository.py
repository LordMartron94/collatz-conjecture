import time

from src.storage.database import Database
from src.utils.utils import print_time


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

    def get_calculation(self):
        query = """SELECT * FROM collatz_main_data ORDER BY calculation_count DESC"""

        results = self.database.fetch_one_in_query(query)

        if not results:
            return None

        return results

    def get_junction_data_by_number(self, number):
        query = (
            """SELECT * FROM number_to_sequence WHERE number_id=%s AND step_count=0"""
            % number
        )

        results = self.database.read_query(query)

        if not results:
            return None

        return results

    # def get_sequences_number_is_in_by_number(self, number: int):
    #     query = """
    #         SELECT sequence_id FROM number_to_sequence WHERE number_id = %s;
    #     """
    #
    #     args = (number,)
    #     sequence_ids = self.database.query(query, args=args)
    #
    #     return sequence_ids

    def get_number_sequence_by_number(self, number: int) -> tuple:
        query = """
                    SELECT sequence_id FROM number_to_sequence WHERE number_id = %s AND step_count=0;
                """

        args = (number,)
        sequence_ids = self.database.fetch_one_in_query(query, args)

        return sequence_ids

    def get_numbers_by_sequence(self, sequence_id: int):
        query = """
                    SELECT number_id FROM number_to_sequence WHERE sequence_id = %s;
                """

        args = (sequence_id,)
        numbers = self.database.read_query(query, args=args)

        return numbers

    def insert_new_sequence(self):
        query = """
        INSERT INTO collatz_sequence_data (_null)
        VALUES (%s);
        """

        args = ("None",)

        sequence_id = self.database.query(query, args)

        return sequence_id

    def insert_new_junction_entry(self, number: int, sequence_id: int, step_count: int):
        query = """INSERT INTO number_to_sequence (number_id, sequence_id, step_count)
        VALUES (%s, %s, %s)"""

        args = (number, sequence_id, step_count)

        self.database.query(query, args)

    def insert_new_number(self, number: int, calculation_count: int):
        # print(f"original step-count: {step_count}")

        query = """
                    INSERT INTO collatz_main_data (number, calculation_count, reached_loop)
                    VALUES ( %s, %s, 0)
                """

        args = (number, calculation_count)

        self.database.query(query, args)

    def set_calculation_count(self, number: int, calculation_count: int):
        query = """
            UPDATE collatz_main_data
            SET calculation_count=%s
            WHERE number = %s;
       """

        args = (calculation_count, number)

        self.database.query(query, args)
        return

    def _check_bool(self, bool_value: bool):
        if bool_value:
            return 1
        if not bool_value:
            return 0

    def set_reached_loop(self, number, reached_loop: bool):
        query = """
                    UPDATE collatz_main_data
                    SET reached_loop=%s
                    WHERE number = %s;
               """

        args = (self._check_bool(reached_loop), number)

        self.database.query(query, args)

    def check_if_junction_entry_already_exists_by_sequence(self, number: int, sequence_id: int) -> bool:
        query = """
                    SELECT sequence_id FROM number_to_sequence WHERE number_id = %s AND sequence_id = %s;
                """

        args = (number, sequence_id,)
        result = self.database.fetch_one_in_query(query, args)

        if result:
            return True
        return False

    def check_if_junction_entry_already_exists_by_step(self, number: int, step_id: int) -> bool:
        # print(number)
        start = time.time()

        query = """
                    SELECT sequence_id FROM number_to_sequence WHERE number_id = %s AND step_count = %s;
                """

        args = (number, step_id,)
        result = self.database.fetch_one_in_query(query, args)

        end = time.time()

        print_time(start, end, f"execute the query")

        if result:
            return True
        return False

    def generate_sequence(self, number) -> [int, None]:
        if not self.check_if_junction_entry_already_exists_by_step(
            number,
            0
        ):
            return self.insert_new_sequence()
        else:
            return None
