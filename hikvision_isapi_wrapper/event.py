from . import session
import json
import threading


class Event(object):
    
    def __init__(self):
        self._stop = False    
    
    def start_listen_events(self, _callback):
        self._callback = _callback
        x = threading.Thread(target=self._start_listen_events,)        
        x.start()

    def stop_listen_events(self):
        self._stop = True
    
    def get_status(self):
        return not self._stop

    def _start_listen_events(self):
        path = '/ISAPI/Event/notification/alertStream'
        response = session.get(path, stream=True)
        response.raise_for_status()
        
        in_header = False             # are we parsing headers at the moment
        grabbing_response = False     # are we grabbing the response at the moment
        response_size = 0             # the response size that we take from Content-Length
        response_buffer = b""         # where we keep the reponse bytes

        for chunk in response.iter_lines():
            decoded = ""
            try:
                decoded = chunk.decode("utf-8")
            except:
                # image bytes here ignore them
                continue

            if decoded == "--MIME_boundary":                
                in_header = True

            if in_header:
                if decoded.startswith("Content-Length"):
                    decoded.replace(" ", "")
                    content_length = decoded.split(":")[1]
                    response_size = int(content_length)

                if decoded == "":
                    in_header = False
                    grabbing_response = True

            elif grabbing_response:
                response_buffer += chunk

                if len(response_buffer) != response_size:
                    response_buffer += b"\n"
                else:
                    # time to convert it json and return it
                    grabbing_response = False
                    print(response_buffer)
                    dic = json.loads(response_buffer)
                    
                    if dic["eventType"] == "AccessControllerEvent":
                        rsp = {
                            "date": dic["dateTime"],
                            "status": dic["AccessControllerEvent"]["attendanceStatus"],
                        }
                        if rsp["status"] == "checkIn":
                            rsp["employee_id"] = int(dic["AccessControllerEvent"]["employeeNoString"])
                        self._callback(rsp)
                    response_buffer = b""
                    if self._stop:
                        return 0
