import os
from requests.auth import HTTPDigestAuth
from .tools import LiveServerSession


HIKVISION_ACT_LOGIN = 'admin'
HIKVISION_ACT_PASSWORD = 'o123123G'
HIKVISION_ACT_HOST = 'http://192.168.0.251'
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