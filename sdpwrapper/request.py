from pydantic import BaseModel
import requests

from config import config


def view_request(request_id: int ):
    url = config.get('URL') + f"/requests/{request_id}"
    response = requests.get(url, headers=config.get('HEADERS'))
    return response.json().get('request')


class SDPRequest(BaseModel):
    id: int
    subject: str


class Request():
    @staticmethod
    def get(id):
        return SDPRequest(**view_request(id))
