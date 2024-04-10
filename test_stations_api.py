import pytest
import logging

logger = logging.getLogger(__name__)


# This Test verifies the compliance of stations = ['1', '2', '3', '4', '5'],this tests verifies if each station has
# correct version,interval and can set the values correctly.
@pytest.mark.parametrize("station_id", ['1', '2', '3', '4', '5'])
def test_station_compliance(command_enum, test_help, station_id):
    is_version_correct = test_help.verify_version(station_id, command_enum.GET_VERSION.value)
    is_interval_correct = test_help.verify_interval(station_id, command_enum.GET_INTERVAL.value)
    is_able_to_set_value = test_help.set_value(station_id, command_enum.SET_VALUES.value)
    assert is_version_correct, f'Version is incorrect'
    assert is_interval_correct, f'Interval is incorrect'
    assert is_able_to_set_value, f'could not set value'


# This Test verifies the setValue method with different types of payload ie null, string and number.
# For this test we are using only station number 2.
@pytest.mark.parametrize("n_value", [1, "", 10, 5, 13, "load"])
def test_set_value(command_enum, test_help, n_value):
    is_able_to_set_value = test_help.set_value(2, command_enum.SET_VALUES.value, n_value)
    assert is_able_to_set_value, f'could not set value'
