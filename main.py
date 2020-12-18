import hikvision_wrapper as client

# person = Person('192.168.0.251', False)
# print(person.search(1))

person_instance = client.Person()
person = person_instance.search('4')
print(person.UserInfoSearch.UserInfo[0].name)
new_person = person_instance.add(6, 'test6', 'normal', '12345', 'male')
print(new_person)



