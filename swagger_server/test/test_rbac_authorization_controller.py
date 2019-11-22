# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_group import IoK8sApimachineryPkgApisMetaV1APIGroup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRbacAuthorizationController(BaseTestCase):
    """RbacAuthorizationController integration test stubs"""

    def test_get_rbac_authorization_api_group(self):
        """Test case for get_rbac_authorization_api_group

        
        """
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
