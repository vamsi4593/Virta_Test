import pytest
from enum import Enum
from lib.lib_test_helper import Helper


class Status(Enum):
    OK = 'ok'
    FAIL = 'fail'


class Command(str, Enum):
    GET_VERSION = "getVersion"
    GET_INTERVAL = "getInterval"
    SET_VALUES = "setValues"


@pytest.fixture
def status_enum():
    return Status


@pytest.fixture
def command_enum():
    return Command


@pytest.fixture(scope="session")
def test_help():
    helper_instance = Helper()
    return helper_instance
