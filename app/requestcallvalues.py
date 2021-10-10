class requestCallValues:
    def __init__(self):
        self.headers = ''

    @property
    def headers(self):
        return self.headers

    @headers.setter
    def headers(self, headers):
        self.headers = headers
