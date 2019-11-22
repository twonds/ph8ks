# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_authorization_v1beta1_local_subject_access_review import IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_self_subject_access_review import IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_self_subject_rules_review import IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_subject_access_review import IoK8sApiAuthorizationV1beta1SubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthorizationV1beta1Controller(BaseTestCase):
    """AuthorizationV1beta1Controller integration test stubs"""

    def test_create_authorization_v1beta1_namespaced_local_subject_access_review(self):
        """Test case for create_authorization_v1beta1_namespaced_local_subject_access_review

        
        """
        body = IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/authorization.k8s.io/v1beta1/namespaces/{namespace}/localsubjectaccessreviews'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_authorization_v1beta1_self_subject_access_review(self):
        """Test case for create_authorization_v1beta1_self_subject_access_review

        
        """
        body = IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/authorization.k8s.io/v1beta1/selfsubjectaccessreviews',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_authorization_v1beta1_self_subject_rules_review(self):
        """Test case for create_authorization_v1beta1_self_subject_rules_review

        
        """
        body = IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/authorization.k8s.io/v1beta1/selfsubjectrulesreviews',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_authorization_v1beta1_subject_access_review(self):
        """Test case for create_authorization_v1beta1_subject_access_review

        
        """
        body = IoK8sApiAuthorizationV1beta1SubjectAccessReview()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/authorization.k8s.io/v1beta1/subjectaccessreviews',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_authorization_v1beta1_api_resources(self):
        """Test case for get_authorization_v1beta1_api_resources

        
        """
        response = self.client.open(
            '/apis/authorization.k8s.io/v1beta1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
