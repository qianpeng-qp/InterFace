import mock
def mock_test(url, request_data, method, response_data):
    mock_method = mock.Mock(return_value=response_data)
    result = mock_method(url, method, request_data)
    return result




