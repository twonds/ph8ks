# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1beta1_custom_resource_definition import IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinition  # noqa: E501
from swagger_server.models.io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1beta1_custom_resource_definition_list import IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApiextensionsV1beta1Controller(BaseTestCase):
    """ApiextensionsV1beta1Controller integration test stubs"""

    def test_create_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for create_apiextensions_v1beta1_custom_resource_definition

        
        """
        body = IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinition()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apiextensions_v1beta1_collection_custom_resource_definition(self):
        """Test case for delete_apiextensions_v1beta1_collection_custom_resource_definition

        
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
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for delete_apiextensions_v1beta1_custom_resource_definition

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_apiextensions_v1beta1_api_resources(self):
        """Test case for get_apiextensions_v1beta1_api_resources

        
        """
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for list_apiextensions_v1beta1_custom_resource_definition

        
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
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for patch_apiextensions_v1beta1_custom_resource_definition

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apiextensions_v1beta1_custom_resource_definition_status(self):
        """Test case for patch_apiextensions_v1beta1_custom_resource_definition_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for read_apiextensions_v1beta1_custom_resource_definition

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apiextensions_v1beta1_custom_resource_definition_status(self):
        """Test case for read_apiextensions_v1beta1_custom_resource_definition_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for replace_apiextensions_v1beta1_custom_resource_definition

        
        """
        body = IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinition()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apiextensions_v1beta1_custom_resource_definition_status(self):
        """Test case for replace_apiextensions_v1beta1_custom_resource_definition_status

        
        """
        body = IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinition()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apiextensions_v1beta1_custom_resource_definition(self):
        """Test case for watch_apiextensions_v1beta1_custom_resource_definition

        
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
            '/apis/apiextensions.k8s.io/v1beta1/watch/customresourcedefinitions/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apiextensions_v1beta1_custom_resource_definition_list(self):
        """Test case for watch_apiextensions_v1beta1_custom_resource_definition_list

        
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
            '/apis/apiextensions.k8s.io/v1beta1/watch/customresourcedefinitions',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()