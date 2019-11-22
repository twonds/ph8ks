# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.io_k8s_api_authentication_v1_token_request import IoK8sApiAuthenticationV1TokenRequest  # noqa: E501
from swagger_server.models.io_k8s_api_autoscaling_v1_scale import IoK8sApiAutoscalingV1Scale  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_binding import IoK8sApiCoreV1Binding  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_component_status import IoK8sApiCoreV1ComponentStatus  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_component_status_list import IoK8sApiCoreV1ComponentStatusList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_config_map import IoK8sApiCoreV1ConfigMap  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_config_map_list import IoK8sApiCoreV1ConfigMapList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_endpoints import IoK8sApiCoreV1Endpoints  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_endpoints_list import IoK8sApiCoreV1EndpointsList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_event import IoK8sApiCoreV1Event  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_event_list import IoK8sApiCoreV1EventList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_limit_range import IoK8sApiCoreV1LimitRange  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_limit_range_list import IoK8sApiCoreV1LimitRangeList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_namespace import IoK8sApiCoreV1Namespace  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_namespace_list import IoK8sApiCoreV1NamespaceList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_node import IoK8sApiCoreV1Node  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_node_list import IoK8sApiCoreV1NodeList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_persistent_volume import IoK8sApiCoreV1PersistentVolume  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_persistent_volume_claim import IoK8sApiCoreV1PersistentVolumeClaim  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_persistent_volume_claim_list import IoK8sApiCoreV1PersistentVolumeClaimList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_persistent_volume_list import IoK8sApiCoreV1PersistentVolumeList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_pod import IoK8sApiCoreV1Pod  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_pod_list import IoK8sApiCoreV1PodList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_pod_template import IoK8sApiCoreV1PodTemplate  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_pod_template_list import IoK8sApiCoreV1PodTemplateList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_replication_controller import IoK8sApiCoreV1ReplicationController  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_replication_controller_list import IoK8sApiCoreV1ReplicationControllerList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_resource_quota import IoK8sApiCoreV1ResourceQuota  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_resource_quota_list import IoK8sApiCoreV1ResourceQuotaList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_secret import IoK8sApiCoreV1Secret  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_secret_list import IoK8sApiCoreV1SecretList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_service import IoK8sApiCoreV1Service  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_service_account import IoK8sApiCoreV1ServiceAccount  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_service_account_list import IoK8sApiCoreV1ServiceAccountList  # noqa: E501
from swagger_server.models.io_k8s_api_core_v1_service_list import IoK8sApiCoreV1ServiceList  # noqa: E501
from swagger_server.models.io_k8s_api_policy_v1beta1_eviction import IoK8sApiPolicyV1beta1Eviction  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCoreV1Controller(BaseTestCase):
    """CoreV1Controller integration test stubs"""

    def test_connect_core_v1_delete_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_delete_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_delete_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_delete_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_delete_namespaced_service_proxy(self):
        """Test case for connect_core_v1_delete_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_delete_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_delete_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_delete_node_proxy(self):
        """Test case for connect_core_v1_delete_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_delete_node_proxy_with_path(self):
        """Test case for connect_core_v1_delete_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='DELETE',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_pod_attach(self):
        """Test case for connect_core_v1_get_namespaced_pod_attach

        
        """
        query_string = [('container', 'container_example'),
                        ('stderr', true),
                        ('stdin', true),
                        ('stdout', true),
                        ('tty', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/attach'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_pod_exec(self):
        """Test case for connect_core_v1_get_namespaced_pod_exec

        
        """
        query_string = [('command', 'command_example'),
                        ('container', 'container_example'),
                        ('stderr', true),
                        ('stdin', true),
                        ('stdout', true),
                        ('tty', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/exec'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_pod_portforward(self):
        """Test case for connect_core_v1_get_namespaced_pod_portforward

        
        """
        query_string = [('ports', 56)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/portforward'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_get_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_get_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_service_proxy(self):
        """Test case for connect_core_v1_get_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_get_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_node_proxy(self):
        """Test case for connect_core_v1_get_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_get_node_proxy_with_path(self):
        """Test case for connect_core_v1_get_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_head_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_head_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_namespaced_service_proxy(self):
        """Test case for connect_core_v1_head_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_head_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_node_proxy(self):
        """Test case for connect_core_v1_head_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_head_node_proxy_with_path(self):
        """Test case for connect_core_v1_head_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='HEAD',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_options_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_options_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_namespaced_service_proxy(self):
        """Test case for connect_core_v1_options_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_options_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_node_proxy(self):
        """Test case for connect_core_v1_options_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_options_node_proxy_with_path(self):
        """Test case for connect_core_v1_options_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='OPTIONS',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_patch_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_patch_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_namespaced_service_proxy(self):
        """Test case for connect_core_v1_patch_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_patch_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_node_proxy(self):
        """Test case for connect_core_v1_patch_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_patch_node_proxy_with_path(self):
        """Test case for connect_core_v1_patch_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='PATCH',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_pod_attach(self):
        """Test case for connect_core_v1_post_namespaced_pod_attach

        
        """
        query_string = [('container', 'container_example'),
                        ('stderr', true),
                        ('stdin', true),
                        ('stdout', true),
                        ('tty', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/attach'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_pod_exec(self):
        """Test case for connect_core_v1_post_namespaced_pod_exec

        
        """
        query_string = [('command', 'command_example'),
                        ('container', 'container_example'),
                        ('stderr', true),
                        ('stdin', true),
                        ('stdout', true),
                        ('tty', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/exec'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_pod_portforward(self):
        """Test case for connect_core_v1_post_namespaced_pod_portforward

        
        """
        query_string = [('ports', 56)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/portforward'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_post_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_post_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_service_proxy(self):
        """Test case for connect_core_v1_post_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_post_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_node_proxy(self):
        """Test case for connect_core_v1_post_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_post_node_proxy_with_path(self):
        """Test case for connect_core_v1_post_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='POST',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_namespaced_pod_proxy(self):
        """Test case for connect_core_v1_put_namespaced_pod_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_namespaced_pod_proxy_with_path(self):
        """Test case for connect_core_v1_put_namespaced_pod_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_namespaced_service_proxy(self):
        """Test case for connect_core_v1_put_namespaced_service_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_namespaced_service_proxy_with_path(self):
        """Test case for connect_core_v1_put_namespaced_service_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'.format(name='name_example', namespace='namespace_example', path='path_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_node_proxy(self):
        """Test case for connect_core_v1_put_node_proxy

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy'.format(name='name_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_connect_core_v1_put_node_proxy_with_path(self):
        """Test case for connect_core_v1_put_node_proxy_with_path

        
        """
        query_string = [('path2', 'path_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/proxy/{path}'.format(name='name_example', path='path_example'),
            method='PUT',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespace(self):
        """Test case for create_core_v1_namespace

        
        """
        body = IoK8sApiCoreV1Namespace()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_binding(self):
        """Test case for create_core_v1_namespaced_binding

        
        """
        body = IoK8sApiCoreV1Binding()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/bindings'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_config_map(self):
        """Test case for create_core_v1_namespaced_config_map

        
        """
        body = IoK8sApiCoreV1ConfigMap()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/configmaps'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_endpoints(self):
        """Test case for create_core_v1_namespaced_endpoints

        
        """
        body = IoK8sApiCoreV1Endpoints()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/endpoints'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_event(self):
        """Test case for create_core_v1_namespaced_event

        
        """
        body = IoK8sApiCoreV1Event()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/events'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_limit_range(self):
        """Test case for create_core_v1_namespaced_limit_range

        
        """
        body = IoK8sApiCoreV1LimitRange()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/limitranges'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for create_core_v1_namespaced_persistent_volume_claim

        
        """
        body = IoK8sApiCoreV1PersistentVolumeClaim()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_pod(self):
        """Test case for create_core_v1_namespaced_pod

        
        """
        body = IoK8sApiCoreV1Pod()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_pod_binding(self):
        """Test case for create_core_v1_namespaced_pod_binding

        
        """
        body = IoK8sApiCoreV1Binding()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/binding'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_pod_eviction(self):
        """Test case for create_core_v1_namespaced_pod_eviction

        
        """
        body = IoK8sApiPolicyV1beta1Eviction()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/eviction'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_pod_template(self):
        """Test case for create_core_v1_namespaced_pod_template

        
        """
        body = IoK8sApiCoreV1PodTemplate()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/podtemplates'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_replication_controller(self):
        """Test case for create_core_v1_namespaced_replication_controller

        
        """
        body = IoK8sApiCoreV1ReplicationController()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_resource_quota(self):
        """Test case for create_core_v1_namespaced_resource_quota

        
        """
        body = IoK8sApiCoreV1ResourceQuota()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_secret(self):
        """Test case for create_core_v1_namespaced_secret

        
        """
        body = IoK8sApiCoreV1Secret()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/secrets'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_service(self):
        """Test case for create_core_v1_namespaced_service

        
        """
        body = IoK8sApiCoreV1Service()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_service_account(self):
        """Test case for create_core_v1_namespaced_service_account

        
        """
        body = IoK8sApiCoreV1ServiceAccount()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts'.format(namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_namespaced_service_account_token(self):
        """Test case for create_core_v1_namespaced_service_account_token

        
        """
        body = IoK8sApiAuthenticationV1TokenRequest()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts/{name}/token'.format(name='name_example', namespace='namespace_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_node(self):
        """Test case for create_core_v1_node

        
        """
        body = IoK8sApiCoreV1Node()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/nodes',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_core_v1_persistent_volume(self):
        """Test case for create_core_v1_persistent_volume

        
        """
        body = IoK8sApiCoreV1PersistentVolume()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/persistentvolumes',
            method='POST',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_config_map(self):
        """Test case for delete_core_v1_collection_namespaced_config_map

        
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
            '/api/v1/namespaces/{namespace}/configmaps'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_endpoints(self):
        """Test case for delete_core_v1_collection_namespaced_endpoints

        
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
            '/api/v1/namespaces/{namespace}/endpoints'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_event(self):
        """Test case for delete_core_v1_collection_namespaced_event

        
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
            '/api/v1/namespaces/{namespace}/events'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_limit_range(self):
        """Test case for delete_core_v1_collection_namespaced_limit_range

        
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
            '/api/v1/namespaces/{namespace}/limitranges'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_persistent_volume_claim(self):
        """Test case for delete_core_v1_collection_namespaced_persistent_volume_claim

        
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
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_pod(self):
        """Test case for delete_core_v1_collection_namespaced_pod

        
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
            '/api/v1/namespaces/{namespace}/pods'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_pod_template(self):
        """Test case for delete_core_v1_collection_namespaced_pod_template

        
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
            '/api/v1/namespaces/{namespace}/podtemplates'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_replication_controller(self):
        """Test case for delete_core_v1_collection_namespaced_replication_controller

        
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
            '/api/v1/namespaces/{namespace}/replicationcontrollers'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_resource_quota(self):
        """Test case for delete_core_v1_collection_namespaced_resource_quota

        
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
            '/api/v1/namespaces/{namespace}/resourcequotas'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_secret(self):
        """Test case for delete_core_v1_collection_namespaced_secret

        
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
            '/api/v1/namespaces/{namespace}/secrets'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_namespaced_service_account(self):
        """Test case for delete_core_v1_collection_namespaced_service_account

        
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
            '/api/v1/namespaces/{namespace}/serviceaccounts'.format(namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_node(self):
        """Test case for delete_core_v1_collection_node

        
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
            '/api/v1/nodes',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_collection_persistent_volume(self):
        """Test case for delete_core_v1_collection_persistent_volume

        
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
            '/api/v1/persistentvolumes',
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespace(self):
        """Test case for delete_core_v1_namespace

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_config_map(self):
        """Test case for delete_core_v1_namespaced_config_map

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/configmaps/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_endpoints(self):
        """Test case for delete_core_v1_namespaced_endpoints

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/endpoints/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_event(self):
        """Test case for delete_core_v1_namespaced_event

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/events/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_limit_range(self):
        """Test case for delete_core_v1_namespaced_limit_range

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/limitranges/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for delete_core_v1_namespaced_persistent_volume_claim

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_pod(self):
        """Test case for delete_core_v1_namespaced_pod

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_pod_template(self):
        """Test case for delete_core_v1_namespaced_pod_template

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/podtemplates/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_replication_controller(self):
        """Test case for delete_core_v1_namespaced_replication_controller

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_resource_quota(self):
        """Test case for delete_core_v1_namespaced_resource_quota

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_secret(self):
        """Test case for delete_core_v1_namespaced_secret

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/secrets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_service(self):
        """Test case for delete_core_v1_namespaced_service

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_namespaced_service_account(self):
        """Test case for delete_core_v1_namespaced_service_account

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts/{name}'.format(name='name_example', namespace='namespace_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_node(self):
        """Test case for delete_core_v1_node

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_core_v1_persistent_volume(self):
        """Test case for delete_core_v1_persistent_volume

        
        """
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('gracePeriodSeconds', 56),
                        ('orphanDependents', true),
                        ('propagationPolicy', 'propagationPolicy_example')]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_core_v1_api_resources(self):
        """Test case for get_core_v1_api_resources

        
        """
        response = self.client.open(
            '/api/v1/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_component_status(self):
        """Test case for list_core_v1_component_status

        
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
            '/api/v1/componentstatuses',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_config_map_for_all_namespaces(self):
        """Test case for list_core_v1_config_map_for_all_namespaces

        
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
            '/api/v1/configmaps',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_endpoints_for_all_namespaces(self):
        """Test case for list_core_v1_endpoints_for_all_namespaces

        
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
            '/api/v1/endpoints',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_event_for_all_namespaces(self):
        """Test case for list_core_v1_event_for_all_namespaces

        
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
            '/api/v1/events',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_limit_range_for_all_namespaces(self):
        """Test case for list_core_v1_limit_range_for_all_namespaces

        
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
            '/api/v1/limitranges',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespace(self):
        """Test case for list_core_v1_namespace

        
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
            '/api/v1/namespaces',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_config_map(self):
        """Test case for list_core_v1_namespaced_config_map

        
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
            '/api/v1/namespaces/{namespace}/configmaps'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_endpoints(self):
        """Test case for list_core_v1_namespaced_endpoints

        
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
            '/api/v1/namespaces/{namespace}/endpoints'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_event(self):
        """Test case for list_core_v1_namespaced_event

        
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
            '/api/v1/namespaces/{namespace}/events'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_limit_range(self):
        """Test case for list_core_v1_namespaced_limit_range

        
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
            '/api/v1/namespaces/{namespace}/limitranges'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for list_core_v1_namespaced_persistent_volume_claim

        
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
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_pod(self):
        """Test case for list_core_v1_namespaced_pod

        
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
            '/api/v1/namespaces/{namespace}/pods'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_pod_template(self):
        """Test case for list_core_v1_namespaced_pod_template

        
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
            '/api/v1/namespaces/{namespace}/podtemplates'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_replication_controller(self):
        """Test case for list_core_v1_namespaced_replication_controller

        
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
            '/api/v1/namespaces/{namespace}/replicationcontrollers'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_resource_quota(self):
        """Test case for list_core_v1_namespaced_resource_quota

        
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
            '/api/v1/namespaces/{namespace}/resourcequotas'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_secret(self):
        """Test case for list_core_v1_namespaced_secret

        
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
            '/api/v1/namespaces/{namespace}/secrets'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_service(self):
        """Test case for list_core_v1_namespaced_service

        
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
            '/api/v1/namespaces/{namespace}/services'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_namespaced_service_account(self):
        """Test case for list_core_v1_namespaced_service_account

        
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
            '/api/v1/namespaces/{namespace}/serviceaccounts'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_node(self):
        """Test case for list_core_v1_node

        
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
            '/api/v1/nodes',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_persistent_volume(self):
        """Test case for list_core_v1_persistent_volume

        
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
            '/api/v1/persistentvolumes',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_persistent_volume_claim_for_all_namespaces(self):
        """Test case for list_core_v1_persistent_volume_claim_for_all_namespaces

        
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
            '/api/v1/persistentvolumeclaims',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_pod_for_all_namespaces(self):
        """Test case for list_core_v1_pod_for_all_namespaces

        
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
            '/api/v1/pods',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_pod_template_for_all_namespaces(self):
        """Test case for list_core_v1_pod_template_for_all_namespaces

        
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
            '/api/v1/podtemplates',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_replication_controller_for_all_namespaces(self):
        """Test case for list_core_v1_replication_controller_for_all_namespaces

        
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
            '/api/v1/replicationcontrollers',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_resource_quota_for_all_namespaces(self):
        """Test case for list_core_v1_resource_quota_for_all_namespaces

        
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
            '/api/v1/resourcequotas',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_secret_for_all_namespaces(self):
        """Test case for list_core_v1_secret_for_all_namespaces

        
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
            '/api/v1/secrets',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_service_account_for_all_namespaces(self):
        """Test case for list_core_v1_service_account_for_all_namespaces

        
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
            '/api/v1/serviceaccounts',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_core_v1_service_for_all_namespaces(self):
        """Test case for list_core_v1_service_for_all_namespaces

        
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
            '/api/v1/services',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespace(self):
        """Test case for patch_core_v1_namespace

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespace_status(self):
        """Test case for patch_core_v1_namespace_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_config_map(self):
        """Test case for patch_core_v1_namespaced_config_map

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/configmaps/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_endpoints(self):
        """Test case for patch_core_v1_namespaced_endpoints

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/endpoints/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_event(self):
        """Test case for patch_core_v1_namespaced_event

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/events/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_limit_range(self):
        """Test case for patch_core_v1_namespaced_limit_range

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/limitranges/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for patch_core_v1_namespaced_persistent_volume_claim

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_persistent_volume_claim_status(self):
        """Test case for patch_core_v1_namespaced_persistent_volume_claim_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_pod(self):
        """Test case for patch_core_v1_namespaced_pod

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_pod_status(self):
        """Test case for patch_core_v1_namespaced_pod_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_pod_template(self):
        """Test case for patch_core_v1_namespaced_pod_template

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/podtemplates/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_replication_controller(self):
        """Test case for patch_core_v1_namespaced_replication_controller

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_replication_controller_scale(self):
        """Test case for patch_core_v1_namespaced_replication_controller_scale

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_replication_controller_status(self):
        """Test case for patch_core_v1_namespaced_replication_controller_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_resource_quota(self):
        """Test case for patch_core_v1_namespaced_resource_quota

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_resource_quota_status(self):
        """Test case for patch_core_v1_namespaced_resource_quota_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_secret(self):
        """Test case for patch_core_v1_namespaced_secret

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/secrets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_service(self):
        """Test case for patch_core_v1_namespaced_service

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_service_account(self):
        """Test case for patch_core_v1_namespaced_service_account

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_namespaced_service_status(self):
        """Test case for patch_core_v1_namespaced_service_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_node(self):
        """Test case for patch_core_v1_node

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/nodes/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_node_status(self):
        """Test case for patch_core_v1_node_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/nodes/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_persistent_volume(self):
        """Test case for patch_core_v1_persistent_volume

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_core_v1_persistent_volume_status(self):
        """Test case for patch_core_v1_persistent_volume_status

        
        """
        body = IoK8sApimachineryPkgApisMetaV1Patch()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('force', true)]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}/status'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json-patch+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_component_status(self):
        """Test case for read_core_v1_component_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/componentstatuses/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespace(self):
        """Test case for read_core_v1_namespace

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespace_status(self):
        """Test case for read_core_v1_namespace_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_config_map(self):
        """Test case for read_core_v1_namespaced_config_map

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/configmaps/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_endpoints(self):
        """Test case for read_core_v1_namespaced_endpoints

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/endpoints/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_event(self):
        """Test case for read_core_v1_namespaced_event

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/events/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_limit_range(self):
        """Test case for read_core_v1_namespaced_limit_range

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/limitranges/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for read_core_v1_namespaced_persistent_volume_claim

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_persistent_volume_claim_status(self):
        """Test case for read_core_v1_namespaced_persistent_volume_claim_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_pod(self):
        """Test case for read_core_v1_namespaced_pod

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_pod_log(self):
        """Test case for read_core_v1_namespaced_pod_log

        
        """
        query_string = [('container', 'container_example'),
                        ('follow', true),
                        ('insecureSkipTLSVerifyBackend', true),
                        ('limitBytes', 56),
                        ('pretty', 'pretty_example'),
                        ('previous', true),
                        ('sinceSeconds', 56),
                        ('tailLines', 56),
                        ('timestamps', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/log'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_pod_status(self):
        """Test case for read_core_v1_namespaced_pod_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_pod_template(self):
        """Test case for read_core_v1_namespaced_pod_template

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/podtemplates/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_replication_controller(self):
        """Test case for read_core_v1_namespaced_replication_controller

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_replication_controller_scale(self):
        """Test case for read_core_v1_namespaced_replication_controller_scale

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_replication_controller_status(self):
        """Test case for read_core_v1_namespaced_replication_controller_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_resource_quota(self):
        """Test case for read_core_v1_namespaced_resource_quota

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_resource_quota_status(self):
        """Test case for read_core_v1_namespaced_resource_quota_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_secret(self):
        """Test case for read_core_v1_namespaced_secret

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/secrets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_service(self):
        """Test case for read_core_v1_namespaced_service

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_service_account(self):
        """Test case for read_core_v1_namespaced_service_account

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_namespaced_service_status(self):
        """Test case for read_core_v1_namespaced_service_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_node(self):
        """Test case for read_core_v1_node

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/nodes/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_node_status(self):
        """Test case for read_core_v1_node_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_persistent_volume(self):
        """Test case for read_core_v1_persistent_volume

        
        """
        query_string = [('pretty', 'pretty_example'),
                        ('exact', true),
                        ('export', true)]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_core_v1_persistent_volume_status(self):
        """Test case for read_core_v1_persistent_volume_status

        
        """
        query_string = [('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}/status'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespace(self):
        """Test case for replace_core_v1_namespace

        
        """
        body = IoK8sApiCoreV1Namespace()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespace_finalize(self):
        """Test case for replace_core_v1_namespace_finalize

        
        """
        body = IoK8sApiCoreV1Namespace()
        query_string = [('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example'),
                        ('pretty', 'pretty_example')]
        response = self.client.open(
            '/api/v1/namespaces/{name}/finalize'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespace_status(self):
        """Test case for replace_core_v1_namespace_status

        
        """
        body = IoK8sApiCoreV1Namespace()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_config_map(self):
        """Test case for replace_core_v1_namespaced_config_map

        
        """
        body = IoK8sApiCoreV1ConfigMap()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/configmaps/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_endpoints(self):
        """Test case for replace_core_v1_namespaced_endpoints

        
        """
        body = IoK8sApiCoreV1Endpoints()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/endpoints/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_event(self):
        """Test case for replace_core_v1_namespaced_event

        
        """
        body = IoK8sApiCoreV1Event()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/events/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_limit_range(self):
        """Test case for replace_core_v1_namespaced_limit_range

        
        """
        body = IoK8sApiCoreV1LimitRange()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/limitranges/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for replace_core_v1_namespaced_persistent_volume_claim

        
        """
        body = IoK8sApiCoreV1PersistentVolumeClaim()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_persistent_volume_claim_status(self):
        """Test case for replace_core_v1_namespaced_persistent_volume_claim_status

        
        """
        body = IoK8sApiCoreV1PersistentVolumeClaim()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_pod(self):
        """Test case for replace_core_v1_namespaced_pod

        
        """
        body = IoK8sApiCoreV1Pod()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_pod_status(self):
        """Test case for replace_core_v1_namespaced_pod_status

        
        """
        body = IoK8sApiCoreV1Pod()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/pods/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_pod_template(self):
        """Test case for replace_core_v1_namespaced_pod_template

        
        """
        body = IoK8sApiCoreV1PodTemplate()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/podtemplates/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_replication_controller(self):
        """Test case for replace_core_v1_namespaced_replication_controller

        
        """
        body = IoK8sApiCoreV1ReplicationController()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_replication_controller_scale(self):
        """Test case for replace_core_v1_namespaced_replication_controller_scale

        
        """
        body = IoK8sApiAutoscalingV1Scale()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_replication_controller_status(self):
        """Test case for replace_core_v1_namespaced_replication_controller_status

        
        """
        body = IoK8sApiCoreV1ReplicationController()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_resource_quota(self):
        """Test case for replace_core_v1_namespaced_resource_quota

        
        """
        body = IoK8sApiCoreV1ResourceQuota()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_resource_quota_status(self):
        """Test case for replace_core_v1_namespaced_resource_quota_status

        
        """
        body = IoK8sApiCoreV1ResourceQuota()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/resourcequotas/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_secret(self):
        """Test case for replace_core_v1_namespaced_secret

        
        """
        body = IoK8sApiCoreV1Secret()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/secrets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_service(self):
        """Test case for replace_core_v1_namespaced_service

        
        """
        body = IoK8sApiCoreV1Service()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_service_account(self):
        """Test case for replace_core_v1_namespaced_service_account

        
        """
        body = IoK8sApiCoreV1ServiceAccount()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/serviceaccounts/{name}'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_namespaced_service_status(self):
        """Test case for replace_core_v1_namespaced_service_status

        
        """
        body = IoK8sApiCoreV1Service()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/namespaces/{namespace}/services/{name}/status'.format(name='name_example', namespace='namespace_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_node(self):
        """Test case for replace_core_v1_node

        
        """
        body = IoK8sApiCoreV1Node()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_node_status(self):
        """Test case for replace_core_v1_node_status

        
        """
        body = IoK8sApiCoreV1Node()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/nodes/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_persistent_volume(self):
        """Test case for replace_core_v1_persistent_volume

        
        """
        body = IoK8sApiCoreV1PersistentVolume()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_core_v1_persistent_volume_status(self):
        """Test case for replace_core_v1_persistent_volume_status

        
        """
        body = IoK8sApiCoreV1PersistentVolume()
        query_string = [('pretty', 'pretty_example'),
                        ('dryRun', 'dryRun_example'),
                        ('fieldManager', 'fieldManager_example')]
        response = self.client.open(
            '/api/v1/persistentvolumes/{name}/status'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_config_map_list_for_all_namespaces(self):
        """Test case for watch_core_v1_config_map_list_for_all_namespaces

        
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
            '/api/v1/watch/configmaps',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_endpoints_list_for_all_namespaces(self):
        """Test case for watch_core_v1_endpoints_list_for_all_namespaces

        
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
            '/api/v1/watch/endpoints',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_event_list_for_all_namespaces(self):
        """Test case for watch_core_v1_event_list_for_all_namespaces

        
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
            '/api/v1/watch/events',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_limit_range_list_for_all_namespaces(self):
        """Test case for watch_core_v1_limit_range_list_for_all_namespaces

        
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
            '/api/v1/watch/limitranges',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespace(self):
        """Test case for watch_core_v1_namespace

        
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
            '/api/v1/watch/namespaces/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespace_list(self):
        """Test case for watch_core_v1_namespace_list

        
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
            '/api/v1/watch/namespaces',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_config_map(self):
        """Test case for watch_core_v1_namespaced_config_map

        
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
            '/api/v1/watch/namespaces/{namespace}/configmaps/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_config_map_list(self):
        """Test case for watch_core_v1_namespaced_config_map_list

        
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
            '/api/v1/watch/namespaces/{namespace}/configmaps'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_endpoints(self):
        """Test case for watch_core_v1_namespaced_endpoints

        
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
            '/api/v1/watch/namespaces/{namespace}/endpoints/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_endpoints_list(self):
        """Test case for watch_core_v1_namespaced_endpoints_list

        
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
            '/api/v1/watch/namespaces/{namespace}/endpoints'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_event(self):
        """Test case for watch_core_v1_namespaced_event

        
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
            '/api/v1/watch/namespaces/{namespace}/events/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_event_list(self):
        """Test case for watch_core_v1_namespaced_event_list

        
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
            '/api/v1/watch/namespaces/{namespace}/events'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_limit_range(self):
        """Test case for watch_core_v1_namespaced_limit_range

        
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
            '/api/v1/watch/namespaces/{namespace}/limitranges/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_limit_range_list(self):
        """Test case for watch_core_v1_namespaced_limit_range_list

        
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
            '/api/v1/watch/namespaces/{namespace}/limitranges'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_persistent_volume_claim(self):
        """Test case for watch_core_v1_namespaced_persistent_volume_claim

        
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
            '/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_persistent_volume_claim_list(self):
        """Test case for watch_core_v1_namespaced_persistent_volume_claim_list

        
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
            '/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_pod(self):
        """Test case for watch_core_v1_namespaced_pod

        
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
            '/api/v1/watch/namespaces/{namespace}/pods/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_pod_list(self):
        """Test case for watch_core_v1_namespaced_pod_list

        
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
            '/api/v1/watch/namespaces/{namespace}/pods'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_pod_template(self):
        """Test case for watch_core_v1_namespaced_pod_template

        
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
            '/api/v1/watch/namespaces/{namespace}/podtemplates/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_pod_template_list(self):
        """Test case for watch_core_v1_namespaced_pod_template_list

        
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
            '/api/v1/watch/namespaces/{namespace}/podtemplates'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_replication_controller(self):
        """Test case for watch_core_v1_namespaced_replication_controller

        
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
            '/api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_replication_controller_list(self):
        """Test case for watch_core_v1_namespaced_replication_controller_list

        
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
            '/api/v1/watch/namespaces/{namespace}/replicationcontrollers'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_resource_quota(self):
        """Test case for watch_core_v1_namespaced_resource_quota

        
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
            '/api/v1/watch/namespaces/{namespace}/resourcequotas/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_resource_quota_list(self):
        """Test case for watch_core_v1_namespaced_resource_quota_list

        
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
            '/api/v1/watch/namespaces/{namespace}/resourcequotas'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_secret(self):
        """Test case for watch_core_v1_namespaced_secret

        
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
            '/api/v1/watch/namespaces/{namespace}/secrets/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_secret_list(self):
        """Test case for watch_core_v1_namespaced_secret_list

        
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
            '/api/v1/watch/namespaces/{namespace}/secrets'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_service(self):
        """Test case for watch_core_v1_namespaced_service

        
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
            '/api/v1/watch/namespaces/{namespace}/services/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_service_account(self):
        """Test case for watch_core_v1_namespaced_service_account

        
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
            '/api/v1/watch/namespaces/{namespace}/serviceaccounts/{name}'.format(name='name_example', namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_service_account_list(self):
        """Test case for watch_core_v1_namespaced_service_account_list

        
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
            '/api/v1/watch/namespaces/{namespace}/serviceaccounts'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_namespaced_service_list(self):
        """Test case for watch_core_v1_namespaced_service_list

        
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
            '/api/v1/watch/namespaces/{namespace}/services'.format(namespace='namespace_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_node(self):
        """Test case for watch_core_v1_node

        
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
            '/api/v1/watch/nodes/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_node_list(self):
        """Test case for watch_core_v1_node_list

        
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
            '/api/v1/watch/nodes',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_persistent_volume(self):
        """Test case for watch_core_v1_persistent_volume

        
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
            '/api/v1/watch/persistentvolumes/{name}'.format(name='name_example'),
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_persistent_volume_claim_list_for_all_namespaces(self):
        """Test case for watch_core_v1_persistent_volume_claim_list_for_all_namespaces

        
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
            '/api/v1/watch/persistentvolumeclaims',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_persistent_volume_list(self):
        """Test case for watch_core_v1_persistent_volume_list

        
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
            '/api/v1/watch/persistentvolumes',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_pod_list_for_all_namespaces(self):
        """Test case for watch_core_v1_pod_list_for_all_namespaces

        
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
            '/api/v1/watch/pods',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_pod_template_list_for_all_namespaces(self):
        """Test case for watch_core_v1_pod_template_list_for_all_namespaces

        
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
            '/api/v1/watch/podtemplates',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_replication_controller_list_for_all_namespaces(self):
        """Test case for watch_core_v1_replication_controller_list_for_all_namespaces

        
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
            '/api/v1/watch/replicationcontrollers',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_resource_quota_list_for_all_namespaces(self):
        """Test case for watch_core_v1_resource_quota_list_for_all_namespaces

        
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
            '/api/v1/watch/resourcequotas',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_secret_list_for_all_namespaces(self):
        """Test case for watch_core_v1_secret_list_for_all_namespaces

        
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
            '/api/v1/watch/secrets',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_service_account_list_for_all_namespaces(self):
        """Test case for watch_core_v1_service_account_list_for_all_namespaces

        
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
            '/api/v1/watch/serviceaccounts',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_watch_core_v1_service_list_for_all_namespaces(self):
        """Test case for watch_core_v1_service_list_for_all_namespaces

        
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
            '/api/v1/watch/services',
            method='GET',
            content_type='*/*',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
