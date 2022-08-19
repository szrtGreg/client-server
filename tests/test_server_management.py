import pytest
from unittest.mock import Mock

from server_management import ServerManagement
from data_base import DataBase



def test_show_server_info():
    server_management = ServerManagement()
    output = server_management.show_server_info()
    assert output == ('info', 'server v.2')


def test_show_server_uptime():
    server_management = ServerManagement()
    server_management.server_uptime = Mock(return_value='00:00:01')
    output = server_management.show_server_uptime()
    assert output == ('uptime', '00:00:01')

