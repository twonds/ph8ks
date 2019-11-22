# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_flowcontrol_v1alpha1_flow_schema import IoK8sApiFlowcontrolV1alpha1FlowSchema  # noqa: E501
from swagger_server.models.io_k8s_api_flowcontrol_v1alpha1_flow_schema_list import IoK8sApiFlowcontrolV1alpha1FlowSchemaList  # noqa: E501
from swagger_server.models.io_k8s_api_flowcontrol_v1alpha1_priority_level_configuration import IoK8sApiFlowcontrolV1alpha1PriorityLevelConfiguration  # noqa: E501
from swagger_server.models.io_k8s_api_flowcontrol_v1alpha1_priority_level_configuration_list import IoK8sApiFlowcontrolV1alpha1PriorityLevelConfigurationList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFlowcontrolApiserverV1alpha1Controller(BaseTestCase):
    """FlowcontrolApiserverV1alpha1Controller integration test stubs"""

    def test_create_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for create_flowcontrol_apiserver_v1alpha1_flow_schema

        
        """
        body = IoK8sApiFlowcontrolV1alpha1FlowSchema()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for create_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
        """
        body = IoK8sApiFlowcontrolV1alpha1PriorityLevelConfiguration()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_flowcontrol_apiserver_v1alpha1_collection_flow_schema(self):
        """Test case for delete_flowcontrol_apiserver_v1alpha1_collection_flow_schema

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_flowcontrol_apiserver_v1alpha1_collection_priority_level_configuration(self):
        """Test case for delete_flowcontrol_apiserver_v1alpha1_collection_priority_level_configuration

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for delete_flowcontrol_apiserver_v1alpha1_flow_schema

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for delete_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_flowcontrol_apiserver_v1alpha1_api_resources(self):
        """Test case for get_flowcontrol_apiserver_v1alpha1_api_resources

        
        """
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for list_flowcontrol_apiserver_v1alpha1_flow_schema

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for list_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for patch_flowcontrol_apiserver_v1alpha1_flow_schema

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_flowcontrol_apiserver_v1alpha1_flow_schema_status(self):
        """Test case for patch_flowcontrol_apiserver_v1alpha1_flow_schema_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for patch_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status(self):
        """Test case for patch_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for read_flowcontrol_apiserver_v1alpha1_flow_schema

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_flowcontrol_apiserver_v1alpha1_flow_schema_status(self):
        """Test case for read_flowcontrol_apiserver_v1alpha1_flow_schema_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for read_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status(self):
        """Test case for read_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for replace_flowcontrol_apiserver_v1alpha1_flow_schema

        
        """
        body = IoK8sApiFlowcontrolV1alpha1FlowSchema()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_flowcontrol_apiserver_v1alpha1_flow_schema_status(self):
        """Test case for replace_flowcontrol_apiserver_v1alpha1_flow_schema_status

        
        """
        body = IoK8sApiFlowcontrolV1alpha1FlowSchema()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/flowschemas/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for replace_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
        """
        body = IoK8sApiFlowcontrolV1alpha1PriorityLevelConfiguration()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status(self):
        """Test case for replace_flowcontrol_apiserver_v1alpha1_priority_level_configuration_status

        
        """
        body = IoK8sApiFlowcontrolV1alpha1PriorityLevelConfiguration()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/prioritylevelconfigurations/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_flowcontrol_apiserver_v1alpha1_flow_schema(self):
        """Test case for watch_flowcontrol_apiserver_v1alpha1_flow_schema

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/watch/flowschemas/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_flowcontrol_apiserver_v1alpha1_flow_schema_list(self):
        """Test case for watch_flowcontrol_apiserver_v1alpha1_flow_schema_list

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/watch/flowschemas',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_flowcontrol_apiserver_v1alpha1_priority_level_configuration(self):
        """Test case for watch_flowcontrol_apiserver_v1alpha1_priority_level_configuration

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/watch/prioritylevelconfigurations/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_flowcontrol_apiserver_v1alpha1_priority_level_configuration_list(self):
        """Test case for watch_flowcontrol_apiserver_v1alpha1_priority_level_configuration_list

        
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
            '/apis/flowcontrol.apiserver.k8s.io/v1alpha1/watch/prioritylevelconfigurations',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
