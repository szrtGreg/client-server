from datetime import datetime
from turtle import right
from users import User

class ServerManagement():

    @staticmethod
    def recv_msg(conn, buffer=1024, coder='utf-8'):
        return conn.recv(buffer).decode(coder)

    @staticmethod
    def send_msg(conn, msg, coder='utf-8'):
        return conn.send(msg.encode(coder))

    def __init__(self):
        self.version = 'server v.2'
        self.start_time = datetime.now()
        self.commands = {
            'info': 'show server version',
            'stop' : 'stops server',
            'help' : 'show all commands',
            'uptime': 'show server uptime',
            'show': 'show all users'
        }

        self.handlers = {
            'info': self.show_server_info,
            'stop' : self.stop_server,
            'help' : self.show_help,
            'uptime': self.show_server_uptime,
            'show': self.show_all_users,
            'create': self.create_new_user
        }

    def server_uptime(self):
        now = datetime.now()
        uptime = str(now - self.start_time)
        return uptime[:-7]

    def login(self, username, password, role):
        return User(username, password, role)

    def login_to_account(self, data_base, conn):
        credentials = self.recv_msg(conn).split(":")
        role = data_base.check_user_credentials(credentials[0], credentials[1])

        if role:
            authenticated_user = self.login(credentials[0], credentials[1], role)
            self.send_msg(conn, f'{authenticated_user.username} - Login sucessful')
            return authenticated_user
        
        self.send_msg(conn, f'{credentials[0]} does not exists or password do not match! Try again.')
        return None


    def create_user_object(slef, data):
        userdata = data.split(':')
        if len(userdata) == 3 and userdata[2].upper() in ["USER", "ADMIN"]:
            return User(userdata[0], userdata[1], userdata[2])
        return None


### HANDLERS

    def create_new_user(self, conn, data_base, authenticated_user):
        self.send_msg(conn, "username:password:rights")
        recv = self.recv_msg(conn)
        user = self.create_user_object(recv)

        if user:
            if data_base.add_user(user.get_user_data()):
                 return user.username, user.password
            return 'Error', f'{user.username} already exists'
        else:
            return 'Error', 'Invalid data'
        


    def show_all_users(self, conn, data_base):
        users = data_base.show_users()
        return 'show', users


    def show_server_uptime(self, conn, data_base):
        return "uptime", self.server_uptime()

    def show_server_info(self, *args):
        return 'info', f'{self.version}'

    def show_help(self, *args):
        return 'help', self.commands

    def stop_server(self, conn, *args):
        self.send_msg(conn, 'Connection closed')
        print('Connection closed')
