import asyncio
import hikvision_isapi_wrapper as client

# person = Person('192.168.0.251', False)
# print(person.search(1))

# person_instance = client.Person()
# person = person_instance.search('4')
# print(person.UserInfoSearch.UserInfo[0].name)
# new_person = person_instance.add(6, 'test6', 'normal', '12345', 'male')

def callback(event):
    print(event['date'])

# event_instance = client.Event()
# event_instance.start_listen_events(callback)
# print(event_instance.get_status())
# print(event_instance.stop_listen_events())
fd = client.FaceData()
res = fd.face_data_search('blackFD', '1', 39)
print(res)
print('------------------------------------------endofmain-------------------------------------')
