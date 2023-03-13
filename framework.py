from enum import Enum
import pytest

class ServerStatus(Enum):
    HYBRID = 'hybrid'
    CYBRID = 'cybrid'
    KYBRID = 'kybrid'

class BlahServer:
    def __init__(self, server_config):
        self.server_config = server_config

    def connect(self):
        print("Connecting to the server")

    def disconnect(self):
        print("Disconnecting from the server")

    def set_server_status(self, status: ServerStatus):
        print("Setting server status")

    def get_server_status(self):
        print("Getting the server status")

    def wait_for_status(self, status: ServerStatus):
        print("Waiting for the server status to change to one given in the argument")


server_config1 = {'name': 'blahson', 'password': '@#$%^'}

"""
Test Steps:
1. connect the server
2. change the server status to Hybrid
3. verify that the server status has changed
4. disconnect the server


Question 1. Write a python script running the test steps.
Question 2. Write a pytest test for the test steps.
Question 3. Write a pytest test such that the disconnect takes place even if the status of the server fails to change.


"""
@pytest.fixture(scope="function")
def server():
    server = BlahServer(server_config1)
    server.connect()
    yield server
    server.disconnect()

def test_server(server):
    server.set_server_status(ServerStatus.HYBRID)
    server.wait_for_status(ServerStatus.HYBRID)
    assert False

