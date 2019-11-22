# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_batch_v2alpha1_cron_job import IoK8sApiBatchV2alpha1CronJob  # noqa: E501
from swagger_server.models.io_k8s_api_batch_v2alpha1_cron_job_list import IoK8sApiBatchV2alpha1CronJobList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBatchV2alpha1Controller(BaseTestCase):
    """BatchV2alpha1Controller integration test stubs"""

    def test_create_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for create_batch_v2alpha1_namespaced_cron_job

        
        """
        body = IoK8sApiBatchV2alpha1CronJob()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_batch_v2alpha1_collection_namespaced_cron_job(self):
        """Test case for delete_batch_v2alpha1_collection_namespaced_cron_job

        
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
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for delete_batch_v2alpha1_namespaced_cron_job

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_batch_v2alpha1_api_resources(self):
        """Test case for get_batch_v2alpha1_api_resources

        
        """
        response = self.client.open(
            '/apis/batch/v2alpha1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_batch_v2alpha1_cron_job_for_all_namespaces(self):
        """Test case for list_batch_v2alpha1_cron_job_for_all_namespaces

        
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
            '/apis/batch/v2alpha1/cronjobs',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for list_batch_v2alpha1_namespaced_cron_job

        
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
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for patch_batch_v2alpha1_namespaced_cron_job

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_batch_v2alpha1_namespaced_cron_job_status(self):
        """Test case for patch_batch_v2alpha1_namespaced_cron_job_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for read_batch_v2alpha1_namespaced_cron_job

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_batch_v2alpha1_namespaced_cron_job_status(self):
        """Test case for read_batch_v2alpha1_namespaced_cron_job_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for replace_batch_v2alpha1_namespaced_cron_job

        
        """
        body = IoK8sApiBatchV2alpha1CronJob()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_batch_v2alpha1_namespaced_cron_job_status(self):
        """Test case for replace_batch_v2alpha1_namespaced_cron_job_status

        
        """
        body = IoK8sApiBatchV2alpha1CronJob()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_batch_v2alpha1_cron_job_list_for_all_namespaces(self):
        """Test case for watch_batch_v2alpha1_cron_job_list_for_all_namespaces

        
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
            '/apis/batch/v2alpha1/watch/cronjobs',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_batch_v2alpha1_namespaced_cron_job(self):
        """Test case for watch_batch_v2alpha1_namespaced_cron_job

        
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
            '/apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_batch_v2alpha1_namespaced_cron_job_list(self):
        """Test case for watch_batch_v2alpha1_namespaced_cron_job_list

        
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
            '/apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
