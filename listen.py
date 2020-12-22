#!/usr/local/bin/python3

import json
import requests
from requests.auth import HTTPDigestAuth


url = "http://89.236.213.193:3000/ISAPI/Event/notification/alertStream"

print("*** running scanner ***")

with requests.get(url, auth=HTTPDigestAuth('admin', 'o123123G'), stream=True) as r:
    print(str(r))
    r.raise_for_status()

    in_header = False             # are we parsing headers at the moment
    grabbing_response = False     # are we grabbing the response at the moment
    response_size = 0             # the response size that we take from Content-Length
    response_buffer = b""         # where we keep the reponse bytes

    for chunk in r.iter_lines():
        decoded = ""
        try:
            decoded = chunk.decode("utf-8")
        except:
            # image bytes here ignore them
            continue

        if decoded == "--MIME_boundary":
            print("*** new response ***")
            in_header = True

        if in_header:
            if decoded.startswith("Content-Length"):
                decoded.replace(" ", "")
                content_length = decoded.split(":")[1]
                response_size = int(content_length)

                print("-----------")
                print(f"content-length: {response_size} bytes")
                print("-----------")

            if decoded == "":
                in_header = False
                grabbing_response = True

        elif grabbing_response:
            response_buffer += chunk + b"\n"

            # print("*** current buffer size ***")
            # print(len(response_buffer))
            # print(response_buffer)

            if len(response_buffer) >= response_size:
                # time to convert it json and return it
                grabbing_response = False
                dic = json.loads(response_buffer)
                print("*** end of response ***")

                if dic["eventType"] == "AccessControllerEvent":
                    rsp = {
                        "date": dic["dateTime"],
                        "status": dic["AccessControllerEvent"]["attendanceStatus"],
                    }

                    if rsp["status"] == "checkIn":
                        rsp["employee_id"] = int(dic["AccessControllerEvent"]["employeeNoString"])
                    
                    print(rsp)

                response_buffer = b""

        # print(chunk)

