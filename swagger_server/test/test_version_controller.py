# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_apimachinery_pkg_version_info import IoK8sApimachineryPkgVersionInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVersionController(BaseTestCase):
    """VersionController integration test stubs"""

    def test_get_code_version(self):
        """Test case for get_code_version

        
        """
        response = self.client.open(
            '/version/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
