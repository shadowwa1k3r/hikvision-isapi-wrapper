from . import auth
import requests
import json
from types import SimpleNamespace


class FaceDataLib(object):

    def fp_library_add(self, faceLibType, name, customInfo, host):
        path = host+'/ISAPI/Intelligent/FDLib?format=json'
        body = {
            'faceLibType': faceLibType,
            'name': name,
            'customInfo': customInfo
        }
        response = requests.post(path, data=json.dumps(body), auth=auth)
        

        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_update(self, fdid, faceLibType, name, customInfo, host):
        path = f'{host}/ISAPI/Intelligent/FDLib?format=json&FDID={fdid}&faceLibType={faceLibType}'
        body = {
            "name": "CustomTestLibraryBlackFD",
            "customInfo": "test libraryBlackFD"
            }
        response = requests.put(path, data=json.dumps(body), auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_delete(self, fdid, faceLibType, host):
        path = f'{host}/ISAPI/Intelligent/FDLib?format=json&FDID={fdid}&faceLibType={faceLibType}'
        
        response = requests.delete(path, auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_list(self, host):
        path = '{host}/ISAPI/Intelligent/FDLib?format=json'
        response = requests.get(path, auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result


class FaceData(object):
    
    def face_data_add(self, faceLibType, FDID, FPID, name, gender, bornTime, city, faceURL, host1, host2):
        path1 = host1+'/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json'
        path2 = host2+'/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json'
        body = {
            "faceLibType": faceLibType,
            "FDID": str(FDID),
            "FPID": str(FPID),
            "name": name,
            "gender": gender,
            "bornTime": bornTime, #"19940226T000000+0500"
            "city": city,
            "faceURL": faceURL
            }
        response = requests.post(path1, data=json.dumps(body), auth=auth)
        response2 = requests.post(path2, data=json.dumps(body), auth=auth)
        
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def face_data_update(self, faceLibType, FDID, FPID, name, gender, bornTime, city, faceURL, host1, host2):
        path1 = f'{host1}/ISAPI/Intelligent/FDLib/FDSearch?format=json&FDID={FDID}&FPID={FPID}&faceLibType={faceLibType}'
        path2 = f'{host2}/ISAPI/Intelligent/FDLib/FDSearch?format=json&FDID={FDID}&FPID={FPID}&faceLibType={faceLibType}'
        body = {
            "name": name,
            "gender": gender,
            "bornTime": bornTime, #"19940226T000000+0500"
            "city": city,
            "faceURL": faceURL
            }
        response = requests.put(path1, data=json.dumps(body), auth=auth)
        response2 = requests.put(path2, data=json.dumps(body), auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def face_data_delete(self, faceLibType, FDID, FPIDList, host):
        path = f'{host}/ISAPI/Intelligent/FDLib/FDSearch/Delete?format=json&FDID={FDID}&faceLibType={faceLibType}'
        fpidlist = []
        for fpid in FPIDList:
            fpidlist.append({
                'value': fpid
            })
        body = {
            'FPID': fpidlist
            }
             
        response = requests.put(path, data=json.dumps(body), auth=auth)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def face_data_search(self, faceLibType, FDID, FPID, host):
        path = f'{host}/ISAPI/Intelligent/FDLib/FDSearch?format=json'
        body = {
            "searchResultPosition": 0,
            "maxResults": 32,
            "faceLibType": f'{faceLibType}',
            "FDID": f'{FDID}',
            "FPID": f'{FPID}'
            }
        response = requests.post(path, data=json.dumps(body), auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result