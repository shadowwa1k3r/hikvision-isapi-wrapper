from types import SimpleNamespace
import hikvision_isapi_wrapper as api
import vcr


@vcr.use_cassette('tests/vcr_cassettes/fp-data-add.yml', filter_headers=['Authorization'])
def test_fp_data_add():
    fp_lib_instance = api.FaceData()
    response = fp_lib_instance.face_data_add('blackFD', '1', '4', 'tessst', 'male', '19940226T000000+0500', 'Tashkent', 'https://i.ibb.co/P9rJSTQ/murod.jpg')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"


@vcr.use_cassette('tests/vcr_cassettes/fp-data-update.yml', filter_headers=['Authorization'])
def test_fp_data_update():
    fp_lib_instance = api.FaceData()
    response = fp_lib_instance.face_data_update('blackFD', '1', '4', 'tessst', 'male', '19940226T000000+0500', 'Tashkent', 'https://i.ibb.co/P9rJSTQ/murod.jpg')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"


@vcr.use_cassette('tests/vcr_cassettes/fp-data-delete.yml', filter_headers=['Authorization'])
def test_fp_data_delete():
    fp_lib_instance = api.FaceData()
    response = fp_lib_instance.face_data_delete('blackFD', '1', ['4',])
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"
