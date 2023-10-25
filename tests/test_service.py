import pytest
import requests

import source.service as service
import unittest.mock as mock


@mock.patch("source.service.get_user_by_id")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_by_id(1)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mocked_users):
    mock_response = mock.Mock()
    json_data = {"id": 1, "name": "john doe"}
    mock_response.status_code = 200
    mock_response.json.return_value = json_data
    mocked_users.return_value = mock_response
    data = service.get_users()
    assert data == json_data


@mock.patch("requests.get")
def test_get_users_ko(mocked_users):
    mock_response = mock.Mock()
    mock_response.status_code = 401
    mocked_users.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()