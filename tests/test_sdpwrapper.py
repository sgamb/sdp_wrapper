from sdpwrapper import Request
from config import config


def test_request_get():
    """Tests an API call to get something"""

    request = Request.get(1696)

    assert request.id == 1696, "The ID should be in the response_test"
    assert request.subject == 'Разработка пайтон обертки для sdp/sc api'


def test_config():
    """Test that you correctly read enviroment variables from .env file"""
    url = config.get('URL')
    key = config.get('KEY')
    assert isinstance(url, str)
    assert isinstance(key, str)
    assert url == 'https://support.agneko.com/api/v3'
