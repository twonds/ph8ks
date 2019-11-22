# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_autoscaling_v1_horizontal_pod_autoscaler import IoK8sApiAutoscalingV1HorizontalPodAutoscaler  # noqa: E501
from swagger_server.models.io_k8s_api_autoscaling_v1_horizontal_pod_autoscaler_list import IoK8sApiAutoscalingV1HorizontalPodAutoscalerList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAutoscalingV1Controller(BaseTestCase):
    """AutoscalingV1Controller integration test stubs"""

    def test_create_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for create_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
        """
        body = IoK8sApiAutoscalingV1HorizontalPodAutoscaler()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_autoscaling_v1_collection_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v1_collection_namespaced_horizontal_pod_autoscaler

        
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
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_autoscaling_v1_api_resources(self):
        """Test case for get_autoscaling_v1_api_resources

        
        """
        response = self.client.open(
            '/apis/autoscaling/v1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_autoscaling_v1_horizontal_pod_autoscaler_for_all_namespaces(self):
        """Test case for list_autoscaling_v1_horizontal_pod_autoscaler_for_all_namespaces

        
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
            '/apis/autoscaling/v1/horizontalpodautoscalers',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for list_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
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
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for patch_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for patch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for read_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for read_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for replace_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
        """
        body = IoK8sApiAutoscalingV1HorizontalPodAutoscaler()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for replace_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status

        
        """
        body = IoK8sApiAutoscalingV1HorizontalPodAutoscaler()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_autoscaling_v1_horizontal_pod_autoscaler_list_for_all_namespaces(self):
        """Test case for watch_autoscaling_v1_horizontal_pod_autoscaler_list_for_all_namespaces

        
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
            '/apis/autoscaling/v1/watch/horizontalpodautoscalers',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler

        
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
            '/apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_list(self):
        """Test case for watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_list

        
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
            '/apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
