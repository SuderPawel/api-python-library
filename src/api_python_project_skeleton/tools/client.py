import httplib
import socket
import ssl
import sys

import re


def _connect(host, url, method, body, headers, https=False):
    connection = None
    response = None

    try:
        if https:
            connection = httplib.HTTPSConnection(host, context=ssl._create_unverified_context())
        else:
            connection = httplib.HTTPConnection(host)

        host = ('https://%s' % host) if https else ('http://%s' % host)
        sys.stderr.write('%s, %s, %s, %s\n' % (method, host + url, body, headers))
        connection.request(method, host + url, body, headers)

        response = connection.getresponse()
        if not 100 <= response.status < 300:
            raise httplib.HTTPException('Response code is %d' % response.status)

        return response.read()

    except httplib.HTTPException as h_exp:
        sys.stderr.write('HTTP exception: %s\n' % str(h_exp))
        raise h_exp

    except socket.error as s_exp:
        sys.stderr.write('Socket exception: %s\n' % str(s_exp))
        raise s_exp

    finally:
        if response is not None:
            response.close()
        if connection is not None:
            connection.close()


def check_and_set_headers(headers, keys_values):
    for key, value in keys_values.items():
        check_and_set_header(headers, key, value)


def check_and_set_header(headers, key, value):
    if key not in headers and value is not None:
        headers[key] = value


def populate_url_with_arguments(url, arguments):
    for key, value in arguments.items():
        url = re.sub(r"\$\{%s\}" % key, value, url)
    return url


def create_request(host, url, method='GET', body=None, headers=None, https=False):
    _headers = {} if headers is None else headers
    return _connect(host, url, method, body, _headers, https)
