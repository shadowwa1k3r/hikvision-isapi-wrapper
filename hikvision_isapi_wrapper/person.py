from . import session
import json
from types import SimpleNamespace


class Person(object):
    def __init__(self):
        pass

    def search(self, id):
        path = '/ISAPI/AccessControl/UserInfo/Search?format=json'
        body = {
                    "UserInfoSearchCond": {
                        "searchID": "4",
                        "searchResultPosition": 0,
                        "maxResults": 32,
                        "EmployeeNoList":[
                            {
                                "employeeNo": str(id)
                            }
                        ]
                    }
                }
        response = session.post(path, data=json.dumps(body))
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def add(self, id, name, user_type, password, gender):
        path = '/ISAPI/AccessControl/UserInfo/Record?format=json'
        body = {
                    "UserInfo":
                        {
                            "employeeNo":str(id),
                            "name": name,
                            "userType": user_type,
                            "Valid":{
                                "enable": False,
                                "beginTime":"2017-08-01T17:30:08",
                                "endTime":"2022-08-01T17:30:08",
                                "timeType":"local"
                                },
                            
                            "password":password,
                            
                            "gender":gender
                        }
                }
        response = session.post(path, data=json.dumps(body))        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result
    
    def delete(self, id):
        path = '/ISAPI/AccessControl/UserInfo/Delete?format=json'
        body = {
                    "UserInfoDelCond": {                        
                        "EmployeeNoList":[
                            {
                                "employeeNo": str(id)
                            }
                        ]
                    }
                }
        response = session.put(path, data=json.dumps(body))        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def update(self, id, name, user_type, password, gender):
        path = '/ISAPI/AccessControl/UserInfo/Modify?format=json'
        body = {
                    "UserInfo":
                        {
                            "employeeNo":str(id),
                            "name": name,
                            "userType": user_type,
                            "Valid":{
                                "enable": False,
                                "beginTime":"2017-08-01T17:30:08",
                                "endTime":"2022-08-01T17:30:08",
                                "timeType":"local"
                                },
                            
                            "password":password,
                            
                            "gender":gender
                        }
                }
        response = session.put(path, data=json.dumps(body))        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def get_count(self):
        path = '/ISAPI/AccessControl/UserInfo/Count?format=json'
        
        response = session.get(path)        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result.UserInfoCount.userNumber
