from types import SimpleNamespace
import hikvision_isapi_wrapper as api
from pytest import fixture
import vcr

@fixture
def person_keys():
    return ['UserInfoSearch', ]

@vcr.use_cassette('tests/vcr_cassettes/person-search.yml', filter_headers=['Authorization'])
def test_person_search(person_keys):
    """Tests an API call to get a Persons info from access control terminal"""

    person_instance = api.Person()
    response = person_instance.search("4")
    
    assert isinstance(response, SimpleNamespace)
    assert response.UserInfoSearch.UserInfo[0].employeeNo == '4', "This ID should be in response"
    # assert set(person_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/person-add.yml', filter_headers=['Authorization'])
def test_person_add():
    person_instance = api.Person()
    response = person_instance.add(8, 'testid8', 'normal', '12345', 'female')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"

@vcr.use_cassette('tests/vcr_cassettes/person-update.yml', filter_headers=['Authorization'])
def test_person_update():
    person_instance = api.Person()
    response = person_instance.update(8, 'testid888888', 'normal', '12345', 'female')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"

@vcr.use_cassette('tests/vcr_cassettes/person-delete.yml', filter_headers=['Authorization'])
def test_person_delete():
    person_instance = api.Person()
    response = person_instance.delete(8)
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"

@vcr.use_cassette('tests/vcr_cassettes/person-count.yml', filter_headers=['Authorization'])
def test_person_count():
    person_instance = api.Person()
    response = person_instance.get_count()
    assert isinstance(response, int)
    assert response >= 0, "Count should be 0 or greater!"