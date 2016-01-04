import ConfigParser
import sys

from api_python_project_skeleton.tools import client

__author__ = 'paoolo'


def create_request(*args, **kwargs):
    return client.create_req(args, kwargs)


class API(object):
    def __init__(self, *args):
        self.__config = ConfigParser.ConfigParser()
        self.add_config_ini(*args)

    def __getattr__(self, name):
        # noinspection PyBroadException
        try:
            url = self.__config.get(name, 'url')

            def func():
                return create_request(url=url)

            return func
        except Exception as n_exp:
            print('Cannot found API function %s: %s\n' % (name, n_exp))
            return None

    def add_config_ini(self, *args):
        map(lambda config_file_path: self.__config.read(config_file_path), args)


sys.modules[__name__] = API()


def add_config_ini(*args):
    sys.modules[__name__].add_config_ini(*args)
