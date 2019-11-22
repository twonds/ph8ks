# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLogsController(BaseTestCase):
    """LogsController integration test stubs"""

    def test_log_file_handler(self):
        """Test case for log_file_handler

        
        """
        response = self.client.open(
            '/logs/{logpath}'.format(logpath='logpath_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_log_file_list_handler(self):
        """Test case for log_file_list_handler

        
        """
        response = self.client.open(
            '/logs/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
