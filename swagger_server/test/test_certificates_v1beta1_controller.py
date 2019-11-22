# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_certificates_v1beta1_certificate_signing_request import IoK8sApiCertificatesV1beta1CertificateSigningRequest  # noqa: E501
from swagger_server.models.io_k8s_api_certificates_v1beta1_certificate_signing_request_list import IoK8sApiCertificatesV1beta1CertificateSigningRequestList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCertificatesV1beta1Controller(BaseTestCase):
    """CertificatesV1beta1Controller integration test stubs"""

    def test_create_certificates_v1beta1_certificate_signing_request(self):
        """Test case for create_certificates_v1beta1_certificate_signing_request

        
        """
        body = IoK8sApiCertificatesV1beta1CertificateSigningRequest()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_certificates_v1beta1_certificate_signing_request(self):
        """Test case for delete_certificates_v1beta1_certificate_signing_request

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_certificates_v1beta1_collection_certificate_signing_request(self):
        """Test case for delete_certificates_v1beta1_collection_certificate_signing_request

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('allowWatchBookmarks', true),
                        ('_continue', '_continue_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldSelector', 'fieldSelector_example'),
                        ('gracePeriodSeconds', 56),
                        ('labelSelector', 'labelSelector_example'),
                        ('limit', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example'),
                        ('resourceVersion', 'resourceVersion_example'),
                        ('timeoutSeconds', 56),
                        ('watch', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_certificates_v1beta1_api_resources(self):
        """Test case for get_certificates_v1beta1_api_resources

        
        """
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_certificates_v1beta1_certificate_signing_request(self):
        """Test case for list_certificates_v1beta1_certificate_signing_request

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('allowWatchBookmarks', true),
                        ('_continue', '_continue_example'),
                        ('fieldSelector', 'fieldSelector_example'),
                        ('labelSelector', 'labelSelector_example'),
                        ('limit', 56),
                        ('resourceVersion', 'resourceVersion_example'),
                        ('timeoutSeconds', 56),
                        ('watch', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_certificates_v1beta1_certificate_signing_request(self):
        """Test case for patch_certificates_v1beta1_certificate_signing_request

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_certificates_v1beta1_certificate_signing_request_status(self):
        """Test case for patch_certificates_v1beta1_certificate_signing_request_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_certificates_v1beta1_certificate_signing_request(self):
        """Test case for read_certificates_v1beta1_certificate_signing_request

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_certificates_v1beta1_certificate_signing_request_status(self):
        """Test case for read_certificates_v1beta1_certificate_signing_request_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_certificates_v1beta1_certificate_signing_request(self):
        """Test case for replace_certificates_v1beta1_certificate_signing_request

        
        """
        body = IoK8sApiCertificatesV1beta1CertificateSigningRequest()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_certificates_v1beta1_certificate_signing_request_approval(self):
        """Test case for replace_certificates_v1beta1_certificate_signing_request_approval

        
        """
        body = IoK8sApiCertificatesV1beta1CertificateSigningRequest()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/approval'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_certificates_v1beta1_certificate_signing_request_status(self):
        """Test case for replace_certificates_v1beta1_certificate_signing_request_status

        
        """
        body = IoK8sApiCertificatesV1beta1CertificateSigningRequest()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_certificates_v1beta1_certificate_signing_request(self):
        """Test case for watch_certificates_v1beta1_certificate_signing_request

        
        """
        query_string = [('allowWatchBookmarks', true),
                        ('_continue', '_continue_example'),
                        ('fieldSelector', 'fieldSelector_example'),
                        ('labelSelector', 'labelSelector_example'),
                        ('limit', 56),
                        ('pretty', 'pretty_example'),
                        ('resourceVersion', 'resourceVersion_example'),
                        ('timeoutSeconds', 56),
                        ('watch', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/watch/certificatesigningrequests/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_certificates_v1beta1_certificate_signing_request_list(self):
        """Test case for watch_certificates_v1beta1_certificate_signing_request_list

        
        """
        query_string = [('allowWatchBookmarks', true),
                        ('_continue', '_continue_example'),
                        ('fieldSelector', 'fieldSelector_example'),
                        ('labelSelector', 'labelSelector_example'),
                        ('limit', 56),
                        ('pretty', 'pretty_example'),
                        ('resourceVersion', 'resourceVersion_example'),
                        ('timeoutSeconds', 56),
                        ('watch', true)]
        response = self.client.open(
            '/apis/certificates.k8s.io/v1beta1/watch/certificatesigningrequests',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
