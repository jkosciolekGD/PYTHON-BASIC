"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     make_request('https://www.google.com')
     200, 'response data'
"""
import pytest
import requests
from typing import Tuple
from requests_mock import Mocker


def make_request(url: str) -> Tuple[int, str]:
    response = requests.get(url)
    code = response.status_code
    content = response.text
    return code, content


# if __name__ == '__main__':
#     print(make_request('https://www.google.com'))


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""


def test_make_request():
    expected_content = "Content"

    with Mocker() as mocker:
        url = "https://example.com"
        mocker.get(url, text=expected_content)

        code, content = make_request(url)

        assert code == 200
        assert content == expected_content
