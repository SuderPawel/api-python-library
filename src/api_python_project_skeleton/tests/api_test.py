import sys
import unittest

import mock

from api_python_project_skeleton.tools import api


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.host, self.arguments = mock.Mock(), mock.Mock()
        self.body, self.headers = mock.Mock(), mock.Mock()
        self.client_mock = mock.Mock()
        sys.modules['api_python_project_skeleton.tools'] = self.client_mock

    def tearDown(self):
        pass


class GetRequestTestCase(ApiTestCase):
    def setUp(self):
        super(GetRequestTestCase, self).setUp()
        method_name = 'get_test'
        api._API__config.add_section(method_name)
        api._API__config.set(method_name, 'url', '/test')
        api._API__config.set(method_name, 'method', 'GET')

    def runTest(self):
        api.get_test(self.host, self.arguments, self.body, self.headers)
        self.client_mock.client.check_and_set_headers.assert_called_with({}, self.headers)
        self.client_mock.client.create_request.assert_called_with(
                self.host, self.client_mock.client.populate_url_with_arguments(), 'GET', self.body, {}, False)


class PostRequestTestCases(ApiTestCase):
    def setUp(self):
        super(PostRequestTestCases, self).setUp()
        method_name = 'post_test'
        api._API__config.add_section(method_name)
        api._API__config.set(method_name, 'url', '/test')
        api._API__config.set(method_name, 'method', 'POST')

    def runTest(self):
        api.post_test(self.host, self.arguments, self.body, self.headers)
        self.client_mock.client.check_and_set_headers.assert_called_with({}, self.headers)
        self.client_mock.client.create_request.assert_called_with(
                self.host, self.client_mock.client.populate_url_with_arguments(), 'POST', self.body, {}, False)


class PutRequestTestCases(ApiTestCase):
    def setUp(self):
        super(PutRequestTestCases, self).setUp()
        method_name = 'put_test'
        api._API__config.add_section(method_name)
        api._API__config.set(method_name, 'url', '/test')
        api._API__config.set(method_name, 'method', 'PUT')

    def runTest(self):
        api.put_test(self.host, self.arguments, self.body, self.headers)
        self.client_mock.client.check_and_set_headers.assert_called_with({}, self.headers)
        self.client_mock.client.create_request.assert_called_with(
                self.host, self.client_mock.client.populate_url_with_arguments(), 'PUT', self.body, {}, False)


class DeleteRequestTestCases(ApiTestCase):
    def setUp(self):
        super(DeleteRequestTestCases, self).setUp()
        method_name = 'delete_test'
        api._API__config.add_section(method_name)
        api._API__config.set(method_name, 'url', '/test')
        api._API__config.set(method_name, 'method', 'DELETE')

    def runTest(self):
        api.delete_test(self.host, self.arguments, self.body, self.headers)
        self.client_mock.client.check_and_set_headers.assert_called_with({}, self.headers)
        self.client_mock.client.create_request.assert_called_with(
                self.host, self.client_mock.client.populate_url_with_arguments(), 'DELETE', self.body, {}, False)
