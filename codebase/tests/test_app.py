import sys

sys.path.append(".")

from src.api.app import app
from unittest.mock import patch
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@patch("src.api.app.redis_client.get")
def test_get_cache(mock_get):
    mock_get.return_value = "test_value"
    response = client.get("/cache")
    assert response.status_code == 200
    assert response.json() == {"cache": "test_value"}


@patch("src.api.app.redis_client.add")
@patch("src.api.app.get_current_timestamp")
def test_add_cache(mock_timestamp, mock_add):
    mock_timestamp.return_value = "1234567890"
    response = client.post("/cache")
    assert response.status_code == 200
    assert response.json() == {"cache": "Added value to cache successfully"}
    mock_add.assert_called_once_with(value="1234567890 - LOGIN")
