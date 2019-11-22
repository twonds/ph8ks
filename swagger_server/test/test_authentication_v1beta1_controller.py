# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_authentication_v1beta1_token_review import IoK8sApiAuthenticationV1beta1TokenReview  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthenticationV1beta1Controller(BaseTestCase):
    """AuthenticationV1beta1Controller integration test stubs"""

    def test_create_authentication_v1beta1_token_review(self):
        """Test case for create_authentication_v1beta1_token_review

        
        """
        body = IoK8sApiAuthenticationV1beta1TokenReview()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/authentication.k8s.io/v1beta1/tokenreviews',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_authentication_v1beta1_api_resources(self):
        """Test case for get_authentication_v1beta1_api_resources

        
        """
        response = self.client.open(
            '/apis/authentication.k8s.io/v1beta1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
