class Database:
    def __init__(self, connection, db_name: str):
        self.connection = connection
        self.db_name = db_name

    def query(self, sql, args: [str, None]) -> int:
        cursor = self.connection.cursor()

        cursor.execute(sql, args)
        self.connection.commit()

        return cursor.lastrowid

    def read_query(self, query) -> list:
        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchall()

    def new_query(self, query, args: [str, None]) -> list:
        cursor = self.connection.cursor()
        cursor.execute(query, args)

        return cursor.fetchall()

    def table_exists(self, table_name) -> bool:
        result = 0
        query = """
        SELECT * FROM information_schema.tables
        WHERE table_schema = '%s'
            AND table_name = '%s'
        LIMIT 1;""" % (
            self.db_name,
            table_name,
        )
        old_result = self.read_query(query)
        if not old_result:
            # print("Result = []")
            result = None
        if old_result:
            # print("Result is not []")
            result = old_result
        # print(result)
        if result is None:
            # print("There is no result! - Table does not exist! ")
            return False
        # print("There is a result! - Table does exist! ")
        return True

    def fetch_one_in_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()
