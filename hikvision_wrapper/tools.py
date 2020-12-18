from requests import Session
from urllib.parse import urljoin

class LiveServerSession(Session):
    def __init__(self, prefix_url=None, *args, **kwargs):
        super(LiveServerSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url,*args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(LiveServerSession, self).request(method, url, *args, **kwargs)


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
    