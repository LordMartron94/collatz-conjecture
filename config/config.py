class Config:

    @staticmethod
    def get_data() -> dict:
        return {
            'AUTH_SALT': 'my-super-secret-salt',
            'db_user': 'root',
            'db_password': '',
            'db_host': '127.0.0.1',
            'db_name': 'kop_v2'
        }
