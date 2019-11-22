import connexion
import six

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
from swagger_server import util


def connect_core_v1_delete_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_delete_namespaced_pod_proxy

    connect DELETE requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_delete_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_delete_namespaced_pod_proxy_with_path

    connect DELETE requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_delete_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_delete_namespaced_service_proxy

    connect DELETE requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_delete_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_delete_namespaced_service_proxy_with_path

    connect DELETE requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_delete_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_delete_node_proxy

    connect DELETE requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_delete_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_delete_node_proxy_with_path

    connect DELETE requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_pod_attach(name, namespace, container=None, stderr=None, stdin=None, stdout=None, tty=None):  # noqa: E501
    """connect_core_v1_get_namespaced_pod_attach

    connect GET requests to attach of Pod # noqa: E501

    :param name: name of the PodAttachOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param container: The container in which to execute the command. Defaults to only container if there is only one container in the pod.
    :type container: str
    :param stderr: Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true.
    :type stderr: bool
    :param stdin: Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false.
    :type stdin: bool
    :param stdout: Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true.
    :type stdout: bool
    :param tty: TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false.
    :type tty: bool

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_pod_exec(name, namespace, command=None, container=None, stderr=None, stdin=None, stdout=None, tty=None):  # noqa: E501
    """connect_core_v1_get_namespaced_pod_exec

    connect GET requests to exec of Pod # noqa: E501

    :param name: name of the PodExecOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param command: Command is the remote command to execute. argv array. Not executed within a shell.
    :type command: str
    :param container: Container in which to execute the command. Defaults to only container if there is only one container in the pod.
    :type container: str
    :param stderr: Redirect the standard error stream of the pod for this call. Defaults to true.
    :type stderr: bool
    :param stdin: Redirect the standard input stream of the pod for this call. Defaults to false.
    :type stdin: bool
    :param stdout: Redirect the standard output stream of the pod for this call. Defaults to true.
    :type stdout: bool
    :param tty: TTY if true indicates that a tty will be allocated for the exec call. Defaults to false.
    :type tty: bool

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_pod_portforward(name, namespace, ports=None):  # noqa: E501
    """connect_core_v1_get_namespaced_pod_portforward

    connect GET requests to portforward of Pod # noqa: E501

    :param name: name of the PodPortForwardOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param ports: List of ports to forward Required when using WebSockets
    :type ports: int

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_get_namespaced_pod_proxy

    connect GET requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_get_namespaced_pod_proxy_with_path

    connect GET requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_get_namespaced_service_proxy

    connect GET requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_get_namespaced_service_proxy_with_path

    connect GET requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_get_node_proxy

    connect GET requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_get_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_get_node_proxy_with_path

    connect GET requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_head_namespaced_pod_proxy

    connect HEAD requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_head_namespaced_pod_proxy_with_path

    connect HEAD requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_head_namespaced_service_proxy

    connect HEAD requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_head_namespaced_service_proxy_with_path

    connect HEAD requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_head_node_proxy

    connect HEAD requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_head_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_head_node_proxy_with_path

    connect HEAD requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_options_namespaced_pod_proxy

    connect OPTIONS requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_options_namespaced_pod_proxy_with_path

    connect OPTIONS requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_options_namespaced_service_proxy

    connect OPTIONS requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_options_namespaced_service_proxy_with_path

    connect OPTIONS requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_options_node_proxy

    connect OPTIONS requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_options_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_options_node_proxy_with_path

    connect OPTIONS requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_patch_namespaced_pod_proxy

    connect PATCH requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_patch_namespaced_pod_proxy_with_path

    connect PATCH requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_patch_namespaced_service_proxy

    connect PATCH requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_patch_namespaced_service_proxy_with_path

    connect PATCH requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_patch_node_proxy

    connect PATCH requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_patch_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_patch_node_proxy_with_path

    connect PATCH requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_pod_attach(name, namespace, container=None, stderr=None, stdin=None, stdout=None, tty=None):  # noqa: E501
    """connect_core_v1_post_namespaced_pod_attach

    connect POST requests to attach of Pod # noqa: E501

    :param name: name of the PodAttachOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param container: The container in which to execute the command. Defaults to only container if there is only one container in the pod.
    :type container: str
    :param stderr: Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true.
    :type stderr: bool
    :param stdin: Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false.
    :type stdin: bool
    :param stdout: Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true.
    :type stdout: bool
    :param tty: TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false.
    :type tty: bool

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_pod_exec(name, namespace, command=None, container=None, stderr=None, stdin=None, stdout=None, tty=None):  # noqa: E501
    """connect_core_v1_post_namespaced_pod_exec

    connect POST requests to exec of Pod # noqa: E501

    :param name: name of the PodExecOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param command: Command is the remote command to execute. argv array. Not executed within a shell.
    :type command: str
    :param container: Container in which to execute the command. Defaults to only container if there is only one container in the pod.
    :type container: str
    :param stderr: Redirect the standard error stream of the pod for this call. Defaults to true.
    :type stderr: bool
    :param stdin: Redirect the standard input stream of the pod for this call. Defaults to false.
    :type stdin: bool
    :param stdout: Redirect the standard output stream of the pod for this call. Defaults to true.
    :type stdout: bool
    :param tty: TTY if true indicates that a tty will be allocated for the exec call. Defaults to false.
    :type tty: bool

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_pod_portforward(name, namespace, ports=None):  # noqa: E501
    """connect_core_v1_post_namespaced_pod_portforward

    connect POST requests to portforward of Pod # noqa: E501

    :param name: name of the PodPortForwardOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param ports: List of ports to forward Required when using WebSockets
    :type ports: int

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_post_namespaced_pod_proxy

    connect POST requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_post_namespaced_pod_proxy_with_path

    connect POST requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_post_namespaced_service_proxy

    connect POST requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_post_namespaced_service_proxy_with_path

    connect POST requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_post_node_proxy

    connect POST requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_post_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_post_node_proxy_with_path

    connect POST requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_namespaced_pod_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_put_namespaced_pod_proxy

    connect PUT requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the URL path to use for the current proxy request to pod.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_namespaced_pod_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_put_namespaced_pod_proxy_with_path

    connect PUT requests to proxy of Pod # noqa: E501

    :param name: name of the PodProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to pod.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_namespaced_service_proxy(name, namespace, path=None):  # noqa: E501
    """connect_core_v1_put_namespaced_service_proxy

    connect PUT requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_namespaced_service_proxy_with_path(name, namespace, path, path2=None):  # noqa: E501
    """connect_core_v1_put_namespaced_service_proxy_with_path

    connect PUT requests to proxy of Service # noqa: E501

    :param name: name of the ServiceProxyOptions
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_node_proxy(name, path=None):  # noqa: E501
    """connect_core_v1_put_node_proxy

    connect PUT requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: Path is the URL path to use for the current proxy request to node.
    :type path: str

    :rtype: str
    """
    return 'do some magic!'


def connect_core_v1_put_node_proxy_with_path(name, path, path2=None):  # noqa: E501
    """connect_core_v1_put_node_proxy_with_path

    connect PUT requests to proxy of Node # noqa: E501

    :param name: name of the NodeProxyOptions
    :type name: str
    :param path: path to the resource
    :type path: str
    :param path2: Path is the URL path to use for the current proxy request to node.
    :type path2: str

    :rtype: str
    """
    return 'do some magic!'


def create_core_v1_namespace(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespace

    create a Namespace # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Namespace.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_binding(namespace, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_core_v1_namespaced_binding

    create a Binding # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Binding
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Binding.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_config_map(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_config_map

    create a ConfigMap # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ConfigMap
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ConfigMap.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_endpoints(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_endpoints

    create Endpoints # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Endpoints
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Endpoints.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_event(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_event

    create an Event # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Event
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_limit_range(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_limit_range

    create a LimitRange # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1LimitRange
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1LimitRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_persistent_volume_claim(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_persistent_volume_claim

    create a PersistentVolumeClaim # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolumeClaim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_pod(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_pod

    create a Pod # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Pod
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Pod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_pod_binding(name, namespace, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_core_v1_namespaced_pod_binding

    create binding of a Pod # noqa: E501

    :param name: name of the Binding
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Binding
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Binding.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_pod_eviction(name, namespace, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_core_v1_namespaced_pod_eviction

    create eviction of a Pod # noqa: E501

    :param name: name of the Eviction
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiPolicyV1beta1Eviction
    """
    if connexion.request.is_json:
        body = IoK8sApiPolicyV1beta1Eviction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_pod_template(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_pod_template

    create a PodTemplate # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PodTemplate
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PodTemplate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_replication_controller(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_replication_controller

    create a ReplicationController # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ReplicationController.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_resource_quota(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_resource_quota

    create a ResourceQuota # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ResourceQuota.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_secret(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_secret

    create a Secret # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Secret
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Secret.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_service(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_service

    create a Service # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Service
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_service_account(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_namespaced_service_account

    create a ServiceAccount # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ServiceAccount
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ServiceAccount.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_namespaced_service_account_token(name, namespace, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_core_v1_namespaced_service_account_token

    create token of a ServiceAccount # noqa: E501

    :param name: name of the TokenRequest
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthenticationV1TokenRequest
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthenticationV1TokenRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_node(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_node

    create a Node # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Node
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_core_v1_persistent_volume(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_core_v1_persistent_volume

    create a PersistentVolume # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolume.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_config_map(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_config_map

    delete collection of ConfigMap # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_endpoints(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_endpoints

    delete collection of Endpoints # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_event(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_event

    delete collection of Event # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_limit_range(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_limit_range

    delete collection of LimitRange # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_persistent_volume_claim(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_persistent_volume_claim

    delete collection of PersistentVolumeClaim # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_pod(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_pod

    delete collection of Pod # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_pod_template(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_pod_template

    delete collection of PodTemplate # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_replication_controller(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_replication_controller

    delete collection of ReplicationController # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_resource_quota(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_resource_quota

    delete collection of ResourceQuota # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_secret(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_secret

    delete collection of Secret # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_namespaced_service_account(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_namespaced_service_account

    delete collection of ServiceAccount # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_node(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_node

    delete collection of Node # noqa: E501

    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_collection_persistent_volume(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_core_v1_collection_persistent_volume

    delete collection of PersistentVolume # noqa: E501

    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param body: 
    :type body: dict | bytes
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespace(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespace

    delete a Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_config_map(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_config_map

    delete a ConfigMap # noqa: E501

    :param name: name of the ConfigMap
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_endpoints(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_endpoints

    delete Endpoints # noqa: E501

    :param name: name of the Endpoints
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_event(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_event

    delete an Event # noqa: E501

    :param name: name of the Event
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_limit_range(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_limit_range

    delete a LimitRange # noqa: E501

    :param name: name of the LimitRange
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_persistent_volume_claim(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_persistent_volume_claim

    delete a PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_pod(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_pod

    delete a Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_pod_template(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_pod_template

    delete a PodTemplate # noqa: E501

    :param name: name of the PodTemplate
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_replication_controller(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_replication_controller

    delete a ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_resource_quota(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_resource_quota

    delete a ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_secret(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_secret

    delete a Secret # noqa: E501

    :param name: name of the Secret
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_service(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_service

    delete a Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_namespaced_service_account(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_namespaced_service_account

    delete a ServiceAccount # noqa: E501

    :param name: name of the ServiceAccount
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_node(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_node

    delete a Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_core_v1_persistent_volume(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_core_v1_persistent_volume

    delete a PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :type gracePeriodSeconds: int
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :type orphanDependents: bool
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground.
    :type propagationPolicy: str

    :rtype: IoK8sApimachineryPkgApisMetaV1Status
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_core_v1_api_resources():  # noqa: E501
    """get_core_v1_api_resources

    get available resources # noqa: E501


    :rtype: IoK8sApimachineryPkgApisMetaV1APIResourceList
    """
    return 'do some magic!'


def list_core_v1_component_status(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_component_status

    list objects of kind ComponentStatus # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ComponentStatusList
    """
    return 'do some magic!'


def list_core_v1_config_map_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_config_map_for_all_namespaces

    list or watch objects of kind ConfigMap # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ConfigMapList
    """
    return 'do some magic!'


def list_core_v1_endpoints_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_endpoints_for_all_namespaces

    list or watch objects of kind Endpoints # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1EndpointsList
    """
    return 'do some magic!'


def list_core_v1_event_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_event_for_all_namespaces

    list or watch objects of kind Event # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1EventList
    """
    return 'do some magic!'


def list_core_v1_limit_range_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_limit_range_for_all_namespaces

    list or watch objects of kind LimitRange # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1LimitRangeList
    """
    return 'do some magic!'


def list_core_v1_namespace(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespace

    list or watch objects of kind Namespace # noqa: E501

    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1NamespaceList
    """
    return 'do some magic!'


def list_core_v1_namespaced_config_map(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_config_map

    list or watch objects of kind ConfigMap # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ConfigMapList
    """
    return 'do some magic!'


def list_core_v1_namespaced_endpoints(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_endpoints

    list or watch objects of kind Endpoints # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1EndpointsList
    """
    return 'do some magic!'


def list_core_v1_namespaced_event(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_event

    list or watch objects of kind Event # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1EventList
    """
    return 'do some magic!'


def list_core_v1_namespaced_limit_range(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_limit_range

    list or watch objects of kind LimitRange # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1LimitRangeList
    """
    return 'do some magic!'


def list_core_v1_namespaced_persistent_volume_claim(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_persistent_volume_claim

    list or watch objects of kind PersistentVolumeClaim # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeClaimList
    """
    return 'do some magic!'


def list_core_v1_namespaced_pod(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_pod

    list or watch objects of kind Pod # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PodList
    """
    return 'do some magic!'


def list_core_v1_namespaced_pod_template(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_pod_template

    list or watch objects of kind PodTemplate # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PodTemplateList
    """
    return 'do some magic!'


def list_core_v1_namespaced_replication_controller(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_replication_controller

    list or watch objects of kind ReplicationController # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ReplicationControllerList
    """
    return 'do some magic!'


def list_core_v1_namespaced_resource_quota(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_resource_quota

    list or watch objects of kind ResourceQuota # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ResourceQuotaList
    """
    return 'do some magic!'


def list_core_v1_namespaced_secret(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_secret

    list or watch objects of kind Secret # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1SecretList
    """
    return 'do some magic!'


def list_core_v1_namespaced_service(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_service

    list or watch objects of kind Service # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ServiceList
    """
    return 'do some magic!'


def list_core_v1_namespaced_service_account(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_namespaced_service_account

    list or watch objects of kind ServiceAccount # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ServiceAccountList
    """
    return 'do some magic!'


def list_core_v1_node(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_node

    list or watch objects of kind Node # noqa: E501

    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1NodeList
    """
    return 'do some magic!'


def list_core_v1_persistent_volume(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_persistent_volume

    list or watch objects of kind PersistentVolume # noqa: E501

    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeList
    """
    return 'do some magic!'


def list_core_v1_persistent_volume_claim_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_persistent_volume_claim_for_all_namespaces

    list or watch objects of kind PersistentVolumeClaim # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeClaimList
    """
    return 'do some magic!'


def list_core_v1_pod_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_pod_for_all_namespaces

    list or watch objects of kind Pod # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PodList
    """
    return 'do some magic!'


def list_core_v1_pod_template_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_pod_template_for_all_namespaces

    list or watch objects of kind PodTemplate # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1PodTemplateList
    """
    return 'do some magic!'


def list_core_v1_replication_controller_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_replication_controller_for_all_namespaces

    list or watch objects of kind ReplicationController # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ReplicationControllerList
    """
    return 'do some magic!'


def list_core_v1_resource_quota_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_resource_quota_for_all_namespaces

    list or watch objects of kind ResourceQuota # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ResourceQuotaList
    """
    return 'do some magic!'


def list_core_v1_secret_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_secret_for_all_namespaces

    list or watch objects of kind Secret # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1SecretList
    """
    return 'do some magic!'


def list_core_v1_service_account_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_service_account_for_all_namespaces

    list or watch objects of kind ServiceAccount # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ServiceAccountList
    """
    return 'do some magic!'


def list_core_v1_service_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_core_v1_service_for_all_namespaces

    list or watch objects of kind Service # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApiCoreV1ServiceList
    """
    return 'do some magic!'


def patch_core_v1_namespace(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespace

    partially update the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespace_status(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespace_status

    partially update status of the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_config_map(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_config_map

    partially update the specified ConfigMap # noqa: E501

    :param name: name of the ConfigMap
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ConfigMap
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_endpoints(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_endpoints

    partially update the specified Endpoints # noqa: E501

    :param name: name of the Endpoints
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Endpoints
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_event(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_event

    partially update the specified Event # noqa: E501

    :param name: name of the Event
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Event
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_limit_range(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_limit_range

    partially update the specified LimitRange # noqa: E501

    :param name: name of the LimitRange
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1LimitRange
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_persistent_volume_claim(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_persistent_volume_claim

    partially update the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_persistent_volume_claim_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_persistent_volume_claim_status

    partially update status of the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_pod(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_pod

    partially update the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Pod
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_pod_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_pod_status

    partially update status of the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Pod
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_pod_template(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_pod_template

    partially update the specified PodTemplate # noqa: E501

    :param name: name of the PodTemplate
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1PodTemplate
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_replication_controller(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_replication_controller

    partially update the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_replication_controller_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_replication_controller_scale

    partially update scale of the specified ReplicationController # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_replication_controller_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_replication_controller_status

    partially update status of the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_resource_quota(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_resource_quota

    partially update the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_resource_quota_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_resource_quota_status

    partially update status of the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_secret(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_secret

    partially update the specified Secret # noqa: E501

    :param name: name of the Secret
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Secret
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_service(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_service

    partially update the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Service
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_service_account(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_service_account

    partially update the specified ServiceAccount # noqa: E501

    :param name: name of the ServiceAccount
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1ServiceAccount
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_namespaced_service_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_namespaced_service_status

    partially update status of the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Service
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_node(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_node

    partially update the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Node
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_node_status(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_node_status

    partially update status of the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1Node
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_persistent_volume(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_persistent_volume

    partially update the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_core_v1_persistent_volume_status(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_core_v1_persistent_volume_status

    partially update status of the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
    :type fieldManager: str
    :param force: Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
    :type force: bool

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def read_core_v1_component_status(name, pretty=None):  # noqa: E501
    """read_core_v1_component_status

    read the specified ComponentStatus # noqa: E501

    :param name: name of the ComponentStatus
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1ComponentStatus
    """
    return 'do some magic!'


def read_core_v1_namespace(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespace

    read the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Namespace
    """
    return 'do some magic!'


def read_core_v1_namespace_status(name, pretty=None):  # noqa: E501
    """read_core_v1_namespace_status

    read status of the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Namespace
    """
    return 'do some magic!'


def read_core_v1_namespaced_config_map(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_config_map

    read the specified ConfigMap # noqa: E501

    :param name: name of the ConfigMap
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1ConfigMap
    """
    return 'do some magic!'


def read_core_v1_namespaced_endpoints(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_endpoints

    read the specified Endpoints # noqa: E501

    :param name: name of the Endpoints
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Endpoints
    """
    return 'do some magic!'


def read_core_v1_namespaced_event(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_event

    read the specified Event # noqa: E501

    :param name: name of the Event
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Event
    """
    return 'do some magic!'


def read_core_v1_namespaced_limit_range(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_limit_range

    read the specified LimitRange # noqa: E501

    :param name: name of the LimitRange
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1LimitRange
    """
    return 'do some magic!'


def read_core_v1_namespaced_persistent_volume_claim(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_persistent_volume_claim

    read the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    return 'do some magic!'


def read_core_v1_namespaced_persistent_volume_claim_status(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_persistent_volume_claim_status

    read status of the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    return 'do some magic!'


def read_core_v1_namespaced_pod(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_pod

    read the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Pod
    """
    return 'do some magic!'


def read_core_v1_namespaced_pod_log(name, namespace, container=None, follow=None, insecureSkipTLSVerifyBackend=None, limitBytes=None, pretty=None, previous=None, sinceSeconds=None, tailLines=None, timestamps=None):  # noqa: E501
    """read_core_v1_namespaced_pod_log

    read log of the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param container: The container for which to stream logs. Defaults to only container if there is one container in the pod.
    :type container: str
    :param follow: Follow the log stream of the pod. Defaults to false.
    :type follow: bool
    :param insecureSkipTLSVerifyBackend: insecureSkipTLSVerifyBackend indicates that the apiserver should not confirm the validity of the serving certificate of the backend it is connecting to.  This will make the HTTPS connection between the apiserver and the backend insecure. This means the apiserver cannot verify the log data it is receiving came from the real kubelet.  If the kubelet is configured to verify the apiserver&#39;s TLS credentials, it does not mean the connection to the real kubelet is vulnerable to a man in the middle attack (e.g. an attacker could not intercept the actual log data coming from the real kubelet).
    :type insecureSkipTLSVerifyBackend: bool
    :param limitBytes: If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit.
    :type limitBytes: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param previous: Return previous terminated container logs. Defaults to false.
    :type previous: bool
    :param sinceSeconds: A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified.
    :type sinceSeconds: int
    :param tailLines: If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime
    :type tailLines: int
    :param timestamps: If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false.
    :type timestamps: bool

    :rtype: str
    """
    return 'do some magic!'


def read_core_v1_namespaced_pod_status(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_pod_status

    read status of the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Pod
    """
    return 'do some magic!'


def read_core_v1_namespaced_pod_template(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_pod_template

    read the specified PodTemplate # noqa: E501

    :param name: name of the PodTemplate
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1PodTemplate
    """
    return 'do some magic!'


def read_core_v1_namespaced_replication_controller(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_replication_controller

    read the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    return 'do some magic!'


def read_core_v1_namespaced_replication_controller_scale(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_replication_controller_scale

    read scale of the specified ReplicationController # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    return 'do some magic!'


def read_core_v1_namespaced_replication_controller_status(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_replication_controller_status

    read status of the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    return 'do some magic!'


def read_core_v1_namespaced_resource_quota(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_resource_quota

    read the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    return 'do some magic!'


def read_core_v1_namespaced_resource_quota_status(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_resource_quota_status

    read status of the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    return 'do some magic!'


def read_core_v1_namespaced_secret(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_secret

    read the specified Secret # noqa: E501

    :param name: name of the Secret
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Secret
    """
    return 'do some magic!'


def read_core_v1_namespaced_service(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_service

    read the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Service
    """
    return 'do some magic!'


def read_core_v1_namespaced_service_account(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_namespaced_service_account

    read the specified ServiceAccount # noqa: E501

    :param name: name of the ServiceAccount
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1ServiceAccount
    """
    return 'do some magic!'


def read_core_v1_namespaced_service_status(name, namespace, pretty=None):  # noqa: E501
    """read_core_v1_namespaced_service_status

    read status of the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Service
    """
    return 'do some magic!'


def read_core_v1_node(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_node

    read the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1Node
    """
    return 'do some magic!'


def read_core_v1_node_status(name, pretty=None):  # noqa: E501
    """read_core_v1_node_status

    read status of the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Node
    """
    return 'do some magic!'


def read_core_v1_persistent_volume(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_core_v1_persistent_volume

    read the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    return 'do some magic!'


def read_core_v1_persistent_volume_status(name, pretty=None):  # noqa: E501
    """read_core_v1_persistent_volume_status

    read status of the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    return 'do some magic!'


def replace_core_v1_namespace(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespace

    replace the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Namespace.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespace_finalize(name, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """replace_core_v1_namespace_finalize

    replace finalize of the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Namespace.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespace_status(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespace_status

    replace status of the specified Namespace # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Namespace
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Namespace.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_config_map(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_config_map

    replace the specified ConfigMap # noqa: E501

    :param name: name of the ConfigMap
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ConfigMap
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ConfigMap.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_endpoints(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_endpoints

    replace the specified Endpoints # noqa: E501

    :param name: name of the Endpoints
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Endpoints
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Endpoints.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_event(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_event

    replace the specified Event # noqa: E501

    :param name: name of the Event
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Event
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_limit_range(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_limit_range

    replace the specified LimitRange # noqa: E501

    :param name: name of the LimitRange
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1LimitRange
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1LimitRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_persistent_volume_claim(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_persistent_volume_claim

    replace the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolumeClaim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_persistent_volume_claim_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_persistent_volume_claim_status

    replace status of the specified PersistentVolumeClaim # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolumeClaim
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolumeClaim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_pod(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_pod

    replace the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Pod
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Pod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_pod_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_pod_status

    replace status of the specified Pod # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Pod
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Pod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_pod_template(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_pod_template

    replace the specified PodTemplate # noqa: E501

    :param name: name of the PodTemplate
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PodTemplate
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PodTemplate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_replication_controller(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_replication_controller

    replace the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ReplicationController.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_replication_controller_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_replication_controller_scale

    replace scale of the specified ReplicationController # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    if connexion.request.is_json:
        body = IoK8sApiAutoscalingV1Scale.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_replication_controller_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_replication_controller_status

    replace status of the specified ReplicationController # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ReplicationController
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ReplicationController.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_resource_quota(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_resource_quota

    replace the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ResourceQuota.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_resource_quota_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_resource_quota_status

    replace status of the specified ResourceQuota # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ResourceQuota
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ResourceQuota.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_secret(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_secret

    replace the specified Secret # noqa: E501

    :param name: name of the Secret
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Secret
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Secret.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_service(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_service

    replace the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Service
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_service_account(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_service_account

    replace the specified ServiceAccount # noqa: E501

    :param name: name of the ServiceAccount
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1ServiceAccount
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1ServiceAccount.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_namespaced_service_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_namespaced_service_status

    replace status of the specified Service # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Service
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_node(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_node

    replace the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Node
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_node_status(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_node_status

    replace status of the specified Node # noqa: E501

    :param name: name of the Node
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1Node
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_persistent_volume(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_persistent_volume

    replace the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolume.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_core_v1_persistent_volume_status(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_core_v1_persistent_volume_status

    replace status of the specified PersistentVolume # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiCoreV1PersistentVolume
    """
    if connexion.request.is_json:
        body = IoK8sApiCoreV1PersistentVolume.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def watch_core_v1_config_map_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_config_map_list_for_all_namespaces

    watch individual changes to a list of ConfigMap. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_endpoints_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_endpoints_list_for_all_namespaces

    watch individual changes to a list of Endpoints. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_event_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_event_list_for_all_namespaces

    watch individual changes to a list of Event. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_limit_range_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_limit_range_list_for_all_namespaces

    watch individual changes to a list of LimitRange. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespace(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespace

    watch changes to an object of kind Namespace. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Namespace
    :type name: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespace_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespace_list

    watch individual changes to a list of Namespace. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_config_map(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_config_map

    watch changes to an object of kind ConfigMap. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ConfigMap
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_config_map_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_config_map_list

    watch individual changes to a list of ConfigMap. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_endpoints(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_endpoints

    watch changes to an object of kind Endpoints. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Endpoints
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_endpoints_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_endpoints_list

    watch individual changes to a list of Endpoints. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_event(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_event

    watch changes to an object of kind Event. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Event
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_event_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_event_list

    watch individual changes to a list of Event. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_limit_range(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_limit_range

    watch changes to an object of kind LimitRange. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the LimitRange
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_limit_range_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_limit_range_list

    watch individual changes to a list of LimitRange. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_persistent_volume_claim(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_persistent_volume_claim

    watch changes to an object of kind PersistentVolumeClaim. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the PersistentVolumeClaim
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_persistent_volume_claim_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_persistent_volume_claim_list

    watch individual changes to a list of PersistentVolumeClaim. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_pod(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_pod

    watch changes to an object of kind Pod. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Pod
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_pod_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_pod_list

    watch individual changes to a list of Pod. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_pod_template(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_pod_template

    watch changes to an object of kind PodTemplate. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the PodTemplate
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_pod_template_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_pod_template_list

    watch individual changes to a list of PodTemplate. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_replication_controller(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_replication_controller

    watch changes to an object of kind ReplicationController. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ReplicationController
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_replication_controller_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_replication_controller_list

    watch individual changes to a list of ReplicationController. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_resource_quota(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_resource_quota

    watch changes to an object of kind ResourceQuota. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ResourceQuota
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_resource_quota_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_resource_quota_list

    watch individual changes to a list of ResourceQuota. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_secret(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_secret

    watch changes to an object of kind Secret. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Secret
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_secret_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_secret_list

    watch individual changes to a list of Secret. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_service(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_service

    watch changes to an object of kind Service. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Service
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_service_account(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_service_account

    watch changes to an object of kind ServiceAccount. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ServiceAccount
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_service_account_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_service_account_list

    watch individual changes to a list of ServiceAccount. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_namespaced_service_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_namespaced_service_list

    watch individual changes to a list of Service. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_node(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_node

    watch changes to an object of kind Node. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Node
    :type name: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_node_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_node_list

    watch individual changes to a list of Node. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_persistent_volume(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_persistent_volume

    watch changes to an object of kind PersistentVolume. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the PersistentVolume
    :type name: str
    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_persistent_volume_claim_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_persistent_volume_claim_list_for_all_namespaces

    watch individual changes to a list of PersistentVolumeClaim. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_persistent_volume_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_persistent_volume_list

    watch individual changes to a list of PersistentVolume. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_pod_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_pod_list_for_all_namespaces

    watch individual changes to a list of Pod. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_pod_template_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_pod_template_list_for_all_namespaces

    watch individual changes to a list of PodTemplate. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_replication_controller_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_replication_controller_list_for_all_namespaces

    watch individual changes to a list of ReplicationController. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_resource_quota_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_resource_quota_list_for_all_namespaces

    watch individual changes to a list of ResourceQuota. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_secret_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_secret_list_for_all_namespaces

    watch individual changes to a list of Secret. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_service_account_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_service_account_list_for_all_namespaces

    watch individual changes to a list of ServiceAccount. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'


def watch_core_v1_service_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_core_v1_service_list_for_all_namespaces

    watch individual changes to a list of Service. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

    :param allowWatchBookmarks: allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored.
    :type allowWatchBookmarks: bool
    :param _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
    :type _continue: str
    :param fieldSelector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
    :type fieldSelector: str
    :param labelSelector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
    :type labelSelector: str
    :param limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
    :type limit: int
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param resourceVersion: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
    :type resourceVersion: str
    :param timeoutSeconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
    :type timeoutSeconds: int
    :param watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
    :type watch: bool

    :rtype: IoK8sApimachineryPkgApisMetaV1WatchEvent
    """
    return 'do some magic!'
