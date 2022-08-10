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
    
    def create_new_user(self, user_data):
        if self.get_user(user_data['username']) is None:
            with self.connection as connection:
                cursor = connection.cursor()
                query = """INSERT INTO users (name, password, role) VALUES(%s, %s, %s);"""
                cursor.execute(query, (user_data['username'], user_data['password'], user_data['role']))
                print(cursor.statusmessage)
                return True

        return None
    
    def delete_user(self, username):
        if self.get_user(username) is not None:
            with self.connection as connection:
                cursor = connection.cursor()
                query = "DELETE FROM users WHERE name = %s"
                cursor.execute(query, (username,))
                print(cursor.statusmessage)
                return True       
        return None



    def send_message(self, receiver, sender, text):
        if self.get_user(receiver) is not None:
            with self.connection as connection:
                cursor = connection.cursor()
                query = """INSERT INTO messages (sender, receiver, text) VALUES(%s, %s, %s);"""
                cursor.execute(query, (sender, receiver, text[:255].strip()))
                print(cursor.statusmessage)
                return 'OK'
        return None
            




