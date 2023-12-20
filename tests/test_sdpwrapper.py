from sdpwrapper import Request
from sdpwrapper import Task
from config import config


def test_request_get():
    """Tests an API call to get something"""

    request = Request.get(1696)

    assert request.id == 1696, "The ID should be in the response_test"
    assert request.subject == 'Разработка пайтон обертки для sdp/sc api'


def test_task_get():
    """You need to implement get method on Task class"""

    task = Task.get(70)

    assert task.title == 'test task'


def test_config():
    """Test that you correctly read enviroment variables from .env file"""
    url = config.get('URL')
    key = config.get('KEY')
    assert isinstance(url, str)
    assert isinstance(key, str)
    assert url == 'https://support.agneko.com/api/v3'
