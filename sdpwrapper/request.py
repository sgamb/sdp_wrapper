class Request():
    def __init__(self, id):
        self.id = id
        self.subject = 'Разработка пайтон обертки для sdp/sc api'

    def info(self):
        return {'id': self.id, 'subject': self.subject}
