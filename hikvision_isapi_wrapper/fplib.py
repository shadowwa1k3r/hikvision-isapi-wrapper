from . import session
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
        response = session.post(path, data=json.dumps(body))
        

        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_update(self, fdid, faceLibType, name, customInfo, host):
        path = f'{host}/ISAPI/Intelligent/FDLib?format=json&FDID={fdid}&faceLibType={faceLibType}'
        body = {
            "name": "CustomTestLibraryBlackFD",
            "customInfo": "test libraryBlackFD"
            }
        response = session.put(path, data=json.dumps(body))
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_delete(self, fdid, faceLibType, host):
        path = f'{host}/ISAPI/Intelligent/FDLib?format=json&FDID={fdid}&faceLibType={faceLibType}'
        
        response = session.delete(path)
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def fp_library_list(self, host):
        path = '{host}/ISAPI/Intelligent/FDLib?format=json'
        response = session.get(path)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result


class FaceData(object):
    
    def face_data_add(self, faceLibType, FDID, FPID, name, gender, bornTime, city, faceURL, host):
        path = host+'/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json'
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
        response = session.post(path, data=json.dumps(body))
        
        
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result

    def face_data_update(self, faceLibType, FDID, FPID, name, gender, bornTime, city, faceURL, host):
        path = f'{host}/ISAPI/Intelligent/FDLib/FDSearch?format=json&FDID={FDID}&FPID={FPID}&faceLibType={faceLibType}'
        body = {
            "name": name,
            "gender": gender,
            "bornTime": bornTime, #"19940226T000000+0500"
            "city": city,
            "faceURL": faceURL
            }
        response = session.put(path, data=json.dumps(body))
        
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
             
        response = session.put(path, data=json.dumps(body))
        
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
        response = session.post(path, data=json.dumps(body))
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        return result