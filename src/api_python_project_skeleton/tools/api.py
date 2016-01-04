import ConfigParser
import sys


class API(object):
    def __init__(self, *args):
        self.__config = ConfigParser.ConfigParser()
        self.add_api_config(*args)

    def __get(self, name, field, default_value=None):
        if self.__config.has_option(name, field):
            return self.__config.get(name, field)
        else:
            return default_value

    def __get_url(self, name):
        return self.__get(name, 'url', '/')

    def __get_method(self, name):
        return self.__get(name, 'method', 'GET')

    def __get_headers(self, name):
        _headers = self.__get(name, 'headers', '')
        _headers = _headers.split(',')

        headers = {}
        for header in _headers:
            if ':' in header:
                header_key, header_value = header.split(':')
                headers[header_key] = header_value

        return headers

    def __getattr__(self, name):
        # noinspection PyBroadException
        try:
            url = self.__get_url(name)
            method = self.__get_method(name)
            _headers = self.__get_headers(name)

            def inner(host, arguments=None, body=None, headers=None, https=False):
                from api_python_project_skeleton.tools import client

                headers = {} if headers is None else headers
                client.check_and_set_headers(_headers, headers)

                _arguments = {} if arguments is None else arguments
                _url = client.populate_url_with_arguments(url, _arguments)

                return client.create_request(host, _url, method, body, _headers, https)

            return inner

        except Exception as n_exp:
            print('Cannot found API function %s: %s\n' % (name, n_exp))
            return None

    def add_api_config(self, *args):
        map(lambda config_file_path: self.__config.read(config_file_path), args)

    def get_basic_authorization_header(self, user, password):
        import base64
        token = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
        return {'Authorization': 'Basic %s' % token}


sys.modules[__name__] = API()


def add_api_config(*args):
    sys.modules[__name__].add_api_config(*args)


def get_basic_authorization_header(user, password):
    return sys.modules[__name__].get_basic_authorization_header(user, password)
