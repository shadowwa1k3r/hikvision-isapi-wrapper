from types import SimpleNamespace
import hikvision_isapi_wrapper as api
import vcr


@vcr.use_cassette('tests/vcr_cassettes/fplib-add.yml', filter_headers=['Authorization'])
def test_fp_lib_add():
    fp_lib_instance = api.FaceDataLib()
    response = fp_lib_instance.fp_library_add('blackFD', 'testfplib2', 'testcustominfo')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"
    assert response.FDID is not None, "Successfully creating fp library must return FDID field"

@vcr.use_cassette('tests/vcr_cassettes/fplib-update.yml', filter_headers=['Authorization'])
def test_fp_lib_update():
    fp_lib_instance = api.FaceDataLib()
    response = fp_lib_instance.fp_library_update('1', 'blackFD', 'testfplib2', 'testcustominfo')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"

@vcr.use_cassette('tests/vcr_cassettes/fplib-delete.yml', filter_headers=['Authorization'])
def test_fp_lib_delete():
    fp_lib_instance = api.FaceDataLib()
    response = fp_lib_instance.fp_library_delete('1', 'blackFD')
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"


@vcr.use_cassette('tests/vcr_cassettes/fplib-list.yml', filter_headers=['Authorization'])
def test_fp_lib_list():
    fp_lib_instance = api.FaceDataLib()
    response = fp_lib_instance.fp_library_list()
    assert isinstance(response, SimpleNamespace)
    assert response.statusString == 'OK', "Successful response should be OK"
