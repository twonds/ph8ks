# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_rbac_v1alpha1_cluster_role import IoK8sApiRbacV1alpha1ClusterRole  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_cluster_role_binding import IoK8sApiRbacV1alpha1ClusterRoleBinding  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_cluster_role_binding_list import IoK8sApiRbacV1alpha1ClusterRoleBindingList  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_cluster_role_list import IoK8sApiRbacV1alpha1ClusterRoleList  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_role import IoK8sApiRbacV1alpha1Role  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_role_binding import IoK8sApiRbacV1alpha1RoleBinding  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_role_binding_list import IoK8sApiRbacV1alpha1RoleBindingList  # noqa: E501
from swagger_server.models.io_k8s_api_rbac_v1alpha1_role_list import IoK8sApiRbacV1alpha1RoleList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRbacAuthorizationV1alpha1Controller(BaseTestCase):
    """RbacAuthorizationV1alpha1Controller integration test stubs"""

    def test_create_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for create_rbac_authorization_v1alpha1_cluster_role

        
        """
        body = IoK8sApiRbacV1alpha1ClusterRole()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for create_rbac_authorization_v1alpha1_cluster_role_binding

        
        """
        body = IoK8sApiRbacV1alpha1ClusterRoleBinding()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for create_rbac_authorization_v1alpha1_namespaced_role

        
        """
        body = IoK8sApiRbacV1alpha1Role()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for create_rbac_authorization_v1alpha1_namespaced_role_binding

        
        """
        body = IoK8sApiRbacV1alpha1RoleBinding()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for delete_rbac_authorization_v1alpha1_cluster_role

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for delete_rbac_authorization_v1alpha1_cluster_role_binding

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_collection_cluster_role(self):
        """Test case for delete_rbac_authorization_v1alpha1_collection_cluster_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_collection_cluster_role_binding(self):
        """Test case for delete_rbac_authorization_v1alpha1_collection_cluster_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_collection_namespaced_role(self):
        """Test case for delete_rbac_authorization_v1alpha1_collection_namespaced_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_collection_namespaced_role_binding(self):
        """Test case for delete_rbac_authorization_v1alpha1_collection_namespaced_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for delete_rbac_authorization_v1alpha1_namespaced_role

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for delete_rbac_authorization_v1alpha1_namespaced_role_binding

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rbac_authorization_v1alpha1_api_resources(self):
        """Test case for get_rbac_authorization_v1alpha1_api_resources

        
        """
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for list_rbac_authorization_v1alpha1_cluster_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for list_rbac_authorization_v1alpha1_cluster_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for list_rbac_authorization_v1alpha1_namespaced_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for list_rbac_authorization_v1alpha1_namespaced_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_role_binding_for_all_namespaces(self):
        """Test case for list_rbac_authorization_v1alpha1_role_binding_for_all_namespaces

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/rolebindings',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rbac_authorization_v1alpha1_role_for_all_namespaces(self):
        """Test case for list_rbac_authorization_v1alpha1_role_for_all_namespaces

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/roles',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for patch_rbac_authorization_v1alpha1_cluster_role

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for patch_rbac_authorization_v1alpha1_cluster_role_binding

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for patch_rbac_authorization_v1alpha1_namespaced_role

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for patch_rbac_authorization_v1alpha1_namespaced_role_binding

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for read_rbac_authorization_v1alpha1_cluster_role

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for read_rbac_authorization_v1alpha1_cluster_role_binding

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for read_rbac_authorization_v1alpha1_namespaced_role

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for read_rbac_authorization_v1alpha1_namespaced_role_binding

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for replace_rbac_authorization_v1alpha1_cluster_role

        
        """
        body = IoK8sApiRbacV1alpha1ClusterRole()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for replace_rbac_authorization_v1alpha1_cluster_role_binding

        
        """
        body = IoK8sApiRbacV1alpha1ClusterRoleBinding()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for replace_rbac_authorization_v1alpha1_namespaced_role

        
        """
        body = IoK8sApiRbacV1alpha1Role()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for replace_rbac_authorization_v1alpha1_namespaced_role_binding

        
        """
        body = IoK8sApiRbacV1alpha1RoleBinding()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_cluster_role(self):
        """Test case for watch_rbac_authorization_v1alpha1_cluster_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/clusterroles/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_cluster_role_binding(self):
        """Test case for watch_rbac_authorization_v1alpha1_cluster_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/clusterrolebindings/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_cluster_role_binding_list(self):
        """Test case for watch_rbac_authorization_v1alpha1_cluster_role_binding_list

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/clusterrolebindings',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_cluster_role_list(self):
        """Test case for watch_rbac_authorization_v1alpha1_cluster_role_list

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/clusterroles',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_namespaced_role(self):
        """Test case for watch_rbac_authorization_v1alpha1_namespaced_role

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/namespaces/{namespace}/roles/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_namespaced_role_binding(self):
        """Test case for watch_rbac_authorization_v1alpha1_namespaced_role_binding

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/namespaces/{namespace}/rolebindings/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_namespaced_role_binding_list(self):
        """Test case for watch_rbac_authorization_v1alpha1_namespaced_role_binding_list

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/namespaces/{namespace}/rolebindings'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_namespaced_role_list(self):
        """Test case for watch_rbac_authorization_v1alpha1_namespaced_role_list

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/namespaces/{namespace}/roles'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_role_binding_list_for_all_namespaces(self):
        """Test case for watch_rbac_authorization_v1alpha1_role_binding_list_for_all_namespaces

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/rolebindings',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_rbac_authorization_v1alpha1_role_list_for_all_namespaces(self):
        """Test case for watch_rbac_authorization_v1alpha1_role_list_for_all_namespaces

        
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
            '/apis/rbac.authorization.k8s.io/v1alpha1/watch/roles',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
