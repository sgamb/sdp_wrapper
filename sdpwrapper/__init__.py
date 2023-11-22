from dotenv import dotenv_values

from .request import Request  # noqa


config = dotenv_values('.env')
