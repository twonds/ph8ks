# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_versions import IoK8sApimachineryPkgApisMetaV1APIVersions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCoreController(BaseTestCase):
    """CoreController integration test stubs"""

    def test_get_core_api_versions(self):
        """Test case for get_core_api_versions

        
        """
        response = self.client.open(
            '/api/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
