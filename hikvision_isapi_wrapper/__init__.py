import os
from requests.auth import HTTPDigestAuth
from .tools import LiveServerSession


HIKVISION_ACT_LOGIN = os.environ.get('HIKVISION_ACT_LOGIN')
HIKVISION_ACT_PASSWORD = os.environ.get('HIKVISION_ACT_PASSWORD')
HIKVISION_ACT_HOST = os.environ.get('HIKVISION_ACT_HOST')
class LoginPasswordMissingError(Exception):
    pass

if HIKVISION_ACT_LOGIN is None or HIKVISION_ACT_PASSWORD is None:
    raise LoginPasswordMissingError(
        "All Hikvision Access Control Terminals API methods require login and password!"
    )

auth = HTTPDigestAuth(HIKVISION_ACT_LOGIN, HIKVISION_ACT_PASSWORD)
session = LiveServerSession(HIKVISION_ACT_HOST)
session.auth = auth
    

from .person import Person
from .fplib import FaceData, FaceDataLib
from .event import Event