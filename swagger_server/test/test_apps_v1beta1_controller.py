# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_apps_v1beta1_controller_revision import IoK8sApiAppsV1beta1ControllerRevision  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_controller_revision_list import IoK8sApiAppsV1beta1ControllerRevisionList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_deployment import IoK8sApiAppsV1beta1Deployment  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_deployment_list import IoK8sApiAppsV1beta1DeploymentList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_deployment_rollback import IoK8sApiAppsV1beta1DeploymentRollback  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_scale import IoK8sApiAppsV1beta1Scale  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_stateful_set import IoK8sApiAppsV1beta1StatefulSet  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1beta1_stateful_set_list import IoK8sApiAppsV1beta1StatefulSetList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAppsV1beta1Controller(BaseTestCase):
    """AppsV1beta1Controller integration test stubs"""

    def test_create_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for create_apps_v1beta1_namespaced_controller_revision

        
        """
        body = IoK8sApiAppsV1beta1ControllerRevision()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_apps_v1beta1_namespaced_deployment(self):
        """Test case for create_apps_v1beta1_namespaced_deployment

        
        """
        body = IoK8sApiAppsV1beta1Deployment()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_apps_v1beta1_namespaced_deployment_rollback(self):
        """Test case for create_apps_v1beta1_namespaced_deployment_rollback

        
        """
        body = IoK8sApiAppsV1beta1DeploymentRollback()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/rollback'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for create_apps_v1beta1_namespaced_stateful_set

        
        """
        body = IoK8sApiAppsV1beta1StatefulSet()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_collection_namespaced_controller_revision(self):
        """Test case for delete_apps_v1beta1_collection_namespaced_controller_revision

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_collection_namespaced_deployment(self):
        """Test case for delete_apps_v1beta1_collection_namespaced_deployment

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_collection_namespaced_stateful_set(self):
        """Test case for delete_apps_v1beta1_collection_namespaced_stateful_set

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for delete_apps_v1beta1_namespaced_controller_revision

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_namespaced_deployment(self):
        """Test case for delete_apps_v1beta1_namespaced_deployment

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for delete_apps_v1beta1_namespaced_stateful_set

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_apps_v1beta1_api_resources(self):
        """Test case for get_apps_v1beta1_api_resources

        
        """
        response = self.client.open(
            '/apis/apps/v1beta1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_controller_revision_for_all_namespaces(self):
        """Test case for list_apps_v1beta1_controller_revision_for_all_namespaces

        
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
            '/apis/apps/v1beta1/controllerrevisions',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_deployment_for_all_namespaces(self):
        """Test case for list_apps_v1beta1_deployment_for_all_namespaces

        
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
            '/apis/apps/v1beta1/deployments',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for list_apps_v1beta1_namespaced_controller_revision

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_namespaced_deployment(self):
        """Test case for list_apps_v1beta1_namespaced_deployment

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for list_apps_v1beta1_namespaced_stateful_set

        
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
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_apps_v1beta1_stateful_set_for_all_namespaces(self):
        """Test case for list_apps_v1beta1_stateful_set_for_all_namespaces

        
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
            '/apis/apps/v1beta1/statefulsets',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for patch_apps_v1beta1_namespaced_controller_revision

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_deployment(self):
        """Test case for patch_apps_v1beta1_namespaced_deployment

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_deployment_scale(self):
        """Test case for patch_apps_v1beta1_namespaced_deployment_scale

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_deployment_status(self):
        """Test case for patch_apps_v1beta1_namespaced_deployment_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for patch_apps_v1beta1_namespaced_stateful_set

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_stateful_set_scale(self):
        """Test case for patch_apps_v1beta1_namespaced_stateful_set_scale

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_apps_v1beta1_namespaced_stateful_set_status(self):
        """Test case for patch_apps_v1beta1_namespaced_stateful_set_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for read_apps_v1beta1_namespaced_controller_revision

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_deployment(self):
        """Test case for read_apps_v1beta1_namespaced_deployment

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_deployment_scale(self):
        """Test case for read_apps_v1beta1_namespaced_deployment_scale

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_deployment_status(self):
        """Test case for read_apps_v1beta1_namespaced_deployment_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for read_apps_v1beta1_namespaced_stateful_set

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_stateful_set_scale(self):
        """Test case for read_apps_v1beta1_namespaced_stateful_set_scale

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_apps_v1beta1_namespaced_stateful_set_status(self):
        """Test case for read_apps_v1beta1_namespaced_stateful_set_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for replace_apps_v1beta1_namespaced_controller_revision

        
        """
        body = IoK8sApiAppsV1beta1ControllerRevision()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/controllerrevisions/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_deployment(self):
        """Test case for replace_apps_v1beta1_namespaced_deployment

        
        """
        body = IoK8sApiAppsV1beta1Deployment()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_deployment_scale(self):
        """Test case for replace_apps_v1beta1_namespaced_deployment_scale

        
        """
        body = IoK8sApiAppsV1beta1Scale()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_deployment_status(self):
        """Test case for replace_apps_v1beta1_namespaced_deployment_status

        
        """
        body = IoK8sApiAppsV1beta1Deployment()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for replace_apps_v1beta1_namespaced_stateful_set

        
        """
        body = IoK8sApiAppsV1beta1StatefulSet()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_stateful_set_scale(self):
        """Test case for replace_apps_v1beta1_namespaced_stateful_set_scale

        
        """
        body = IoK8sApiAppsV1beta1Scale()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_apps_v1beta1_namespaced_stateful_set_status(self):
        """Test case for replace_apps_v1beta1_namespaced_stateful_set_status

        
        """
        body = IoK8sApiAppsV1beta1StatefulSet()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/apps/v1beta1/namespaces/{namespace}/statefulsets/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_controller_revision_list_for_all_namespaces(self):
        """Test case for watch_apps_v1beta1_controller_revision_list_for_all_namespaces

        
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
            '/apis/apps/v1beta1/watch/controllerrevisions',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_deployment_list_for_all_namespaces(self):
        """Test case for watch_apps_v1beta1_deployment_list_for_all_namespaces

        
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
            '/apis/apps/v1beta1/watch/deployments',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_controller_revision(self):
        """Test case for watch_apps_v1beta1_namespaced_controller_revision

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/controllerrevisions/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_controller_revision_list(self):
        """Test case for watch_apps_v1beta1_namespaced_controller_revision_list

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/controllerrevisions'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_deployment(self):
        """Test case for watch_apps_v1beta1_namespaced_deployment

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/deployments/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_deployment_list(self):
        """Test case for watch_apps_v1beta1_namespaced_deployment_list

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/deployments'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_stateful_set(self):
        """Test case for watch_apps_v1beta1_namespaced_stateful_set

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/statefulsets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_namespaced_stateful_set_list(self):
        """Test case for watch_apps_v1beta1_namespaced_stateful_set_list

        
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
            '/apis/apps/v1beta1/watch/namespaces/{namespace}/statefulsets'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_apps_v1beta1_stateful_set_list_for_all_namespaces(self):
        """Test case for watch_apps_v1beta1_stateful_set_list_for_all_namespaces

        
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
            '/apis/apps/v1beta1/watch/statefulsets',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
