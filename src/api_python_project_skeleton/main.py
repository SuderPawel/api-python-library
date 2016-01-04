import os

from api_python_project_skeleton.tools import config, api

pwd = os.path.dirname(os.path.abspath(__file__))
config.add_config_ini('%s/main.ini' % pwd)
api.add_api_config('%s/api.ini' % pwd)

if __name__ == '__main__':
    authorization_header = api.get_basic_authorization_header(config.user, config.password)
    host = '%s:%s' % (config.host, config.port)

    print api.test(host, arguments={'id': '1'}, headers=authorization_header)
