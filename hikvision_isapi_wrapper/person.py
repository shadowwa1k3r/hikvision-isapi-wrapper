from . import auth
import requests
import json
from types import SimpleNamespace


class Person(object):
    def __init__(self):
        pass

    def search(self, id, host):
        path = host+'/ISAPI/AccessControl/UserInfo/Search?format=json'
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
        response = requests.post(path, data=json.dumps(body), auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def add(self, id, name, user_type, password, gender, doors, host1, host2):
        path1 = host1+'/ISAPI/AccessControl/UserInfo/Record?format=json'
        path2 = host2+'/ISAPI/AccessControl/UserInfo/Record?format=json'
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
                            "doorRight": doors,
                            "RightPlan": [
                                {
                                    "doorNo": 1,
                                    "planTemplateNo": "1"
                                }
                            ],
                            
                            "password":password,
                            
                            "gender":gender
                        }
                }
        response = requests.post(path1, data=json.dumps(body), auth=auth)
        response2 = requests.post(path2, data=json.dumps(body), auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result
    
    def delete(self, id, host):
        path = host+'/ISAPI/AccessControl/UserInfo/Delete?format=json'
        body = {
                    "UserInfoDelCond": {                        
                        "EmployeeNoList":[
                            {
                                "employeeNo": str(id)
                            }
                        ]
                    }
                }
        response = requests.put(path, data=json.dumps(body), auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def update(self, id, name, user_type, password, gender, doors, host1, host2):
        path1 = host1+'/ISAPI/AccessControl/UserInfo/Modify?format=json'
        path2 = host2+'/ISAPI/AccessControl/UserInfo/Modify?format=json'
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
                            "doorRight": doors,
                            "RightPlan": [
                                {
                                    "doorNo": 1,
                                    "planTemplateNo": "1"
                                }
                            ],
                            
                            "password":password,
                            
                            "gender":gender
                        }
                }
        response = requests.put(path1, data=json.dumps(body), auth=auth)
        response2 = requests.put(path2, data=json.dumps(body), auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def get_count(self, host):
        path = host+'/ISAPI/AccessControl/UserInfo/Count?format=json'
        
        response = requests.get(path, auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result.UserInfoCount.userNumber
