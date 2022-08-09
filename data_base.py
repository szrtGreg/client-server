import psycopg2 as ps2


class DataBase:
    def __init__(self, host, database, db_user, password, port):
        self.db_user = db_user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = ps2.connect(
            user=self.db_user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )

    def show_users(self):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM users ;""")
            records = cursor.fetchall()
            print(cursor.statusmessage)
            return records


    def get_user(self, username):
        with self.connection as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM users WHERE name = %s;"""
            cursor.execute(query, (username,))
            record = cursor.fetchone()
            print(cursor.statusmessage)
            return record
    
    
    def check_user_credentials(self, username, password):
        record = self.get_user(username)
        if record is not None and record[2] == password:
            return record[3]
        return None





