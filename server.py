import socket
import json
from configparser import ConfigParser

from server_management import ServerManagement
from data_base import DataBase

### SETTINGS ###
parser = ConfigParser()
parser.read('settings.ini')
params = parser['postgresql']

## CREATE DB ###
data_base = DataBase(params['host'], params['database'], params['user'], params['password'], params['port'])

server_management = ServerManagement()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 65432))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        ### LOGIN ###
        while True:
            try:
                authenticated_user = server_management.login_to_account(data_base, conn)
            except IndexError:
                server_management.send_msg(conn, f'Wrong login or password')
                continue
            if authenticated_user:
                break 

        ### HANDLERS ###
        while True:
            key = server_management.recv_msg(conn)

            try:
                handler = server_management.handlers[key](conn, data_base, authenticated_user)
            except KeyError:
                server_management.send_msg(conn, f'Unsuported command')
                continue
            if key == "stop":
                break
            
            key, value = handler[0], handler[1]
            msg = json.dumps({key: value}, indent=2)
            server_management.send_msg(conn, msg)

