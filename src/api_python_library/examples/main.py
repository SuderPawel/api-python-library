import json
import threading

import os
import re
import tornado.autoreload
import tornado.ioloop
import tornado.web

from api_python_library.tools import config, api


class ItemsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        # items GET /items(.:format) items#index
        items = {'items': [{1: {'title': 'first item'}, 2: {'title': 'second time'}}]}
        self.write(json.dumps(items))
        self.finish()

    def post(self, *args, **kwargs):
        # POST /items(.:format) items#create
        result = {'result': 'ok'}
        self.write(json.dumps(result))
        self.finish()


class ItemHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        # new_item GET /items/new(.:format) items#new
        # item GET /items/:id(.:format) items#show
        # edit_item GET /items/:id/edit(.:format) items#edit
        if re.match(r'/items/new', self.request.path):
            self.write('..nothing to print..')
        elif re.match(r'/items/[0-9]+(/edit)?', self.request.path):
            item = {'title': 'first item'}
            self.write(json.dumps(item))
        self.finish()

    def patch(self, *args, **kwargs):
        # PATCH or PUT /items/:id(.:format) items#update
        result = {'result': 'ok'}
        self.write(json.dumps(result))
        self.finish()

    def put(self, *args, **kwargs):
        # PATCH or PUT /items/:id(.:format) items#update
        result = {'result': 'ok'}
        self.write(json.dumps(result))
        self.finish()

    def delete(self, *args, **kwargs):
        # DELETE /items/:id(.:format) items#destroy
        result = {'result': 'ok'}
        self.write(json.dumps(result))
        self.finish()


pwd = os.path.dirname(os.path.abspath(__file__))
config.add_config_ini('%s/main.ini' % pwd)
api.add_api_config('%s/api.ini' % pwd)

application = tornado.web.Application(
        handlers=[
            (r"/items", ItemsHandler),
            (r"/items/(.*)", ItemHandler),
        ])

if __name__ == '__main__':
    application.listen(config.port, config.host)
    tornado_ioloop = tornado.ioloop.IOLoop.instance()
    threading.Thread(target=tornado_ioloop.start).start()

    authorization_header = api.get_basic_authorization_header(config.user, config.password)
    host = '%s:%s' % (config.host, config.port)

    try:
        print api.index_items(host, headers=authorization_header)
        print api.create_item(host, headers=authorization_header)
        print api.new_item(host, headers=authorization_header)
        print api.edit_item(host, arguments={'id': 1}, headers=authorization_header)
        print api.show_item(host, arguments={'id': 1}, headers=authorization_header)
        print api.update_item(host, arguments={'id': 1}, headers=authorization_header)
        print api.destroy_item(host, arguments={'id': 1}, headers=authorization_header)
    finally:
        tornado_ioloop.stop()
