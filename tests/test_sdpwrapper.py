from sdpwrapper import Request
from sdpwrapper import config


def test_request_info():
    """Tests an API call to get something"""

    request_instance = Request(1696)
    response = request_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1696, "The ID should be in the response_test"
    assert response['subject'] == 'Разработка пайтон обертки для sdp/sc api'


def test_config():
    """Test that you correctly read enviroment variables from .env file"""
    url = config.get('URL')
    key = config.get('KEY')
    assert isinstance(url, str)
    assert isinstance(key, str)
    assert url == 'https://support.agneko.com/api/v3'
