from dotenv import dotenv_values


config = dotenv_values('.env')

HEADERS = {'authtoken': config.get('KEY')}
config.update({'HEADERS': HEADERS})
