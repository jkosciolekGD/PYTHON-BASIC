"""
Write a function which detects if entered string is http/https domain name with optional slash at the end
Restriction: use re module
Note that address may have several domain levels
    is_http_domain('http://wikipedia.org')
    True
    is_http_domain('https://ru.wikipedia.org/')
    True
    is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    pattern = re.compile(r"\bhttps*://[a-z]+[.[a-z]+/*")
    if re.match(pattern, domain):
        return True
    else:
        return False


# if __name__ == '__main__':
#     print(is_http_domain('http://wikipedia.org'))
#     print(is_http_domain('https://wikipedia.org'))
#     print(is_http_domain('wikipedia.org'))
#     print(is_http_domain('https://wikipedia.org/'))



"""
write tests for is_http_domain function
"""


def test_with_http_domain():
    string = 'http://onet.pl'

    assert is_http_domain(string) is True


def test_with_https_domain():
    string = 'https://onet.pl'

    assert is_http_domain(string) is True


def test_with_domain_without_http_or_https():
    string = 'onet.pl'

    assert is_http_domain(string) is False


def test_with_http_domain_with_a_slash_at_the_end():
    string = 'http://onet.pl/'

    assert is_http_domain(string) is True


def test_with_https_domain_with_a_slash_at_the_end():
    string = 'https://onet.pl/'

    assert is_http_domain(string) is True


def test_with_http_domain_with_multiple_domain_level():
    string = 'http://onet.com.pl'

    assert is_http_domain(string) is True


def test_with_https_domain_with_multiple_domain_level():
    string = 'https://onet.com.pl'

    assert is_http_domain(string) is True


def test_with_https_domain_with_multiple_domain_level_with_a_slash():
    string = 'https://onet.com.pl/'

    assert is_http_domain(string) is True


def test_with_http_domain_with_multiple_domain_level_with_a_slash():
    string = 'http://onet.com.pl/'

    assert is_http_domain(string) is True
