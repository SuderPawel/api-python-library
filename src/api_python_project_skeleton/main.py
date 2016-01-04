import os

from api_python_project_skeleton.tools import config, api


pwd = os.path.dirname(os.path.abspath(__file__))
config.add_config_ini('%s/main.ini' % pwd)
api.add_config_ini('%s/tools/api.ini' % pwd)

if __name__ == '__main__':
    print 'Hello World!\nValue for NAME is %s.' % config.NAME
    print api.event()
