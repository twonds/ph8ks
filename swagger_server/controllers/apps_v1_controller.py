import connexion
import six

from swagger_server.models.io_k8s_api_apps_v1_controller_revision import IoK8sApiAppsV1ControllerRevision  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_controller_revision_list import IoK8sApiAppsV1ControllerRevisionList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_daemon_set import IoK8sApiAppsV1DaemonSet  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_daemon_set_list import IoK8sApiAppsV1DaemonSetList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_deployment import IoK8sApiAppsV1Deployment  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_deployment_list import IoK8sApiAppsV1DeploymentList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_replica_set import IoK8sApiAppsV1ReplicaSet  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_replica_set_list import IoK8sApiAppsV1ReplicaSetList  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_stateful_set import IoK8sApiAppsV1StatefulSet  # noqa: E501
from swagger_server.models.io_k8s_api_apps_v1_stateful_set_list import IoK8sApiAppsV1StatefulSetList  # noqa: E501
from swagger_server.models.io_k8s_api_autoscaling_v1_scale import IoK8sApiAutoscalingV1Scale  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server import util


def create_apps_v1_namespaced_controller_revision(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_apps_v1_namespaced_controller_revision

    create a ControllerRevision # noqa: E501

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

    :rtype: IoK8sApiAppsV1ControllerRevision
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1ControllerRevision.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_apps_v1_namespaced_daemon_set(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_apps_v1_namespaced_daemon_set

    create a DaemonSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1DaemonSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_apps_v1_namespaced_deployment(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_apps_v1_namespaced_deployment

    create a Deployment # noqa: E501

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

    :rtype: IoK8sApiAppsV1Deployment
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1Deployment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_apps_v1_namespaced_replica_set(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_apps_v1_namespaced_replica_set

    create a ReplicaSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1ReplicaSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_apps_v1_namespaced_stateful_set(namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_apps_v1_namespaced_stateful_set

    create a StatefulSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1StatefulSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_apps_v1_collection_namespaced_controller_revision(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_apps_v1_collection_namespaced_controller_revision

    delete collection of ControllerRevision # noqa: E501

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


def delete_apps_v1_collection_namespaced_daemon_set(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_apps_v1_collection_namespaced_daemon_set

    delete collection of DaemonSet # noqa: E501

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


def delete_apps_v1_collection_namespaced_deployment(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_apps_v1_collection_namespaced_deployment

    delete collection of Deployment # noqa: E501

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


def delete_apps_v1_collection_namespaced_replica_set(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_apps_v1_collection_namespaced_replica_set

    delete collection of ReplicaSet # noqa: E501

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


def delete_apps_v1_collection_namespaced_stateful_set(namespace, pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_apps_v1_collection_namespaced_stateful_set

    delete collection of StatefulSet # noqa: E501

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


def delete_apps_v1_namespaced_controller_revision(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_apps_v1_namespaced_controller_revision

    delete a ControllerRevision # noqa: E501

    :param name: name of the ControllerRevision
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


def delete_apps_v1_namespaced_daemon_set(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_apps_v1_namespaced_daemon_set

    delete a DaemonSet # noqa: E501

    :param name: name of the DaemonSet
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


def delete_apps_v1_namespaced_deployment(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_apps_v1_namespaced_deployment

    delete a Deployment # noqa: E501

    :param name: name of the Deployment
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


def delete_apps_v1_namespaced_replica_set(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_apps_v1_namespaced_replica_set

    delete a ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
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


def delete_apps_v1_namespaced_stateful_set(name, namespace, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_apps_v1_namespaced_stateful_set

    delete a StatefulSet # noqa: E501

    :param name: name of the StatefulSet
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


def get_apps_v1_api_resources():  # noqa: E501
    """get_apps_v1_api_resources

    get available resources # noqa: E501


    :rtype: IoK8sApimachineryPkgApisMetaV1APIResourceList
    """
    return 'do some magic!'


def list_apps_v1_controller_revision_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_controller_revision_for_all_namespaces

    list or watch objects of kind ControllerRevision # noqa: E501

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

    :rtype: IoK8sApiAppsV1ControllerRevisionList
    """
    return 'do some magic!'


def list_apps_v1_daemon_set_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_daemon_set_for_all_namespaces

    list or watch objects of kind DaemonSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1DaemonSetList
    """
    return 'do some magic!'


def list_apps_v1_deployment_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_deployment_for_all_namespaces

    list or watch objects of kind Deployment # noqa: E501

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

    :rtype: IoK8sApiAppsV1DeploymentList
    """
    return 'do some magic!'


def list_apps_v1_namespaced_controller_revision(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_namespaced_controller_revision

    list or watch objects of kind ControllerRevision # noqa: E501

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

    :rtype: IoK8sApiAppsV1ControllerRevisionList
    """
    return 'do some magic!'


def list_apps_v1_namespaced_daemon_set(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_namespaced_daemon_set

    list or watch objects of kind DaemonSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1DaemonSetList
    """
    return 'do some magic!'


def list_apps_v1_namespaced_deployment(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_namespaced_deployment

    list or watch objects of kind Deployment # noqa: E501

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

    :rtype: IoK8sApiAppsV1DeploymentList
    """
    return 'do some magic!'


def list_apps_v1_namespaced_replica_set(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_namespaced_replica_set

    list or watch objects of kind ReplicaSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1ReplicaSetList
    """
    return 'do some magic!'


def list_apps_v1_namespaced_stateful_set(namespace, pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_namespaced_stateful_set

    list or watch objects of kind StatefulSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1StatefulSetList
    """
    return 'do some magic!'


def list_apps_v1_replica_set_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_replica_set_for_all_namespaces

    list or watch objects of kind ReplicaSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1ReplicaSetList
    """
    return 'do some magic!'


def list_apps_v1_stateful_set_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_apps_v1_stateful_set_for_all_namespaces

    list or watch objects of kind StatefulSet # noqa: E501

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

    :rtype: IoK8sApiAppsV1StatefulSetList
    """
    return 'do some magic!'


def patch_apps_v1_namespaced_controller_revision(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_controller_revision

    partially update the specified ControllerRevision # noqa: E501

    :param name: name of the ControllerRevision
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

    :rtype: IoK8sApiAppsV1ControllerRevision
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_daemon_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_daemon_set

    partially update the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
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

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_daemon_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_daemon_set_status

    partially update status of the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
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

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_deployment(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_deployment

    partially update the specified Deployment # noqa: E501

    :param name: name of the Deployment
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

    :rtype: IoK8sApiAppsV1Deployment
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_deployment_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_deployment_scale

    partially update scale of the specified Deployment # noqa: E501

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


def patch_apps_v1_namespaced_deployment_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_deployment_status

    partially update status of the specified Deployment # noqa: E501

    :param name: name of the Deployment
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

    :rtype: IoK8sApiAppsV1Deployment
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_replica_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_replica_set

    partially update the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
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

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_replica_set_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_replica_set_scale

    partially update scale of the specified ReplicaSet # noqa: E501

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


def patch_apps_v1_namespaced_replica_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_replica_set_status

    partially update status of the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
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

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_stateful_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_stateful_set

    partially update the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
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

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_apps_v1_namespaced_stateful_set_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_stateful_set_scale

    partially update scale of the specified StatefulSet # noqa: E501

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


def patch_apps_v1_namespaced_stateful_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_apps_v1_namespaced_stateful_set_status

    partially update status of the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
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

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def read_apps_v1_namespaced_controller_revision(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_apps_v1_namespaced_controller_revision

    read the specified ControllerRevision # noqa: E501

    :param name: name of the ControllerRevision
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiAppsV1ControllerRevision
    """
    return 'do some magic!'


def read_apps_v1_namespaced_daemon_set(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_apps_v1_namespaced_daemon_set

    read the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    return 'do some magic!'


def read_apps_v1_namespaced_daemon_set_status(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_daemon_set_status

    read status of the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    return 'do some magic!'


def read_apps_v1_namespaced_deployment(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_apps_v1_namespaced_deployment

    read the specified Deployment # noqa: E501

    :param name: name of the Deployment
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiAppsV1Deployment
    """
    return 'do some magic!'


def read_apps_v1_namespaced_deployment_scale(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_deployment_scale

    read scale of the specified Deployment # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    return 'do some magic!'


def read_apps_v1_namespaced_deployment_status(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_deployment_status

    read status of the specified Deployment # noqa: E501

    :param name: name of the Deployment
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAppsV1Deployment
    """
    return 'do some magic!'


def read_apps_v1_namespaced_replica_set(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_apps_v1_namespaced_replica_set

    read the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    return 'do some magic!'


def read_apps_v1_namespaced_replica_set_scale(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_replica_set_scale

    read scale of the specified ReplicaSet # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    return 'do some magic!'


def read_apps_v1_namespaced_replica_set_status(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_replica_set_status

    read status of the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    return 'do some magic!'


def read_apps_v1_namespaced_stateful_set(name, namespace, pretty=None, exact=None, export=None):  # noqa: E501
    """read_apps_v1_namespaced_stateful_set

    read the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    return 'do some magic!'


def read_apps_v1_namespaced_stateful_set_scale(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_stateful_set_scale

    read scale of the specified StatefulSet # noqa: E501

    :param name: name of the Scale
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAutoscalingV1Scale
    """
    return 'do some magic!'


def read_apps_v1_namespaced_stateful_set_status(name, namespace, pretty=None):  # noqa: E501
    """read_apps_v1_namespaced_stateful_set_status

    read status of the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
    :type name: str
    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    return 'do some magic!'


def replace_apps_v1_namespaced_controller_revision(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_controller_revision

    replace the specified ControllerRevision # noqa: E501

    :param name: name of the ControllerRevision
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

    :rtype: IoK8sApiAppsV1ControllerRevision
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1ControllerRevision.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_daemon_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_daemon_set

    replace the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
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

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1DaemonSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_daemon_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_daemon_set_status

    replace status of the specified DaemonSet # noqa: E501

    :param name: name of the DaemonSet
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

    :rtype: IoK8sApiAppsV1DaemonSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1DaemonSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_deployment(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_deployment

    replace the specified Deployment # noqa: E501

    :param name: name of the Deployment
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

    :rtype: IoK8sApiAppsV1Deployment
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1Deployment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_deployment_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_deployment_scale

    replace scale of the specified Deployment # noqa: E501

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


def replace_apps_v1_namespaced_deployment_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_deployment_status

    replace status of the specified Deployment # noqa: E501

    :param name: name of the Deployment
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

    :rtype: IoK8sApiAppsV1Deployment
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1Deployment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_replica_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_replica_set

    replace the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
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

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1ReplicaSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_replica_set_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_replica_set_scale

    replace scale of the specified ReplicaSet # noqa: E501

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


def replace_apps_v1_namespaced_replica_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_replica_set_status

    replace status of the specified ReplicaSet # noqa: E501

    :param name: name of the ReplicaSet
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

    :rtype: IoK8sApiAppsV1ReplicaSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1ReplicaSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_stateful_set(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_stateful_set

    replace the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
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

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1StatefulSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_apps_v1_namespaced_stateful_set_scale(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_stateful_set_scale

    replace scale of the specified StatefulSet # noqa: E501

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


def replace_apps_v1_namespaced_stateful_set_status(name, namespace, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_apps_v1_namespaced_stateful_set_status

    replace status of the specified StatefulSet # noqa: E501

    :param name: name of the StatefulSet
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

    :rtype: IoK8sApiAppsV1StatefulSet
    """
    if connexion.request.is_json:
        body = IoK8sApiAppsV1StatefulSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def watch_apps_v1_controller_revision_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_controller_revision_list_for_all_namespaces

    watch individual changes to a list of ControllerRevision. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_daemon_set_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_daemon_set_list_for_all_namespaces

    watch individual changes to a list of DaemonSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_deployment_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_deployment_list_for_all_namespaces

    watch individual changes to a list of Deployment. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_namespaced_controller_revision(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_controller_revision

    watch changes to an object of kind ControllerRevision. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ControllerRevision
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


def watch_apps_v1_namespaced_controller_revision_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_controller_revision_list

    watch individual changes to a list of ControllerRevision. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_namespaced_daemon_set(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_daemon_set

    watch changes to an object of kind DaemonSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the DaemonSet
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


def watch_apps_v1_namespaced_daemon_set_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_daemon_set_list

    watch individual changes to a list of DaemonSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_namespaced_deployment(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_deployment

    watch changes to an object of kind Deployment. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the Deployment
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


def watch_apps_v1_namespaced_deployment_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_deployment_list

    watch individual changes to a list of Deployment. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_namespaced_replica_set(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_replica_set

    watch changes to an object of kind ReplicaSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the ReplicaSet
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


def watch_apps_v1_namespaced_replica_set_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_replica_set_list

    watch individual changes to a list of ReplicaSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_namespaced_stateful_set(name, namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_stateful_set

    watch changes to an object of kind StatefulSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the StatefulSet
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


def watch_apps_v1_namespaced_stateful_set_list(namespace, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_namespaced_stateful_set_list

    watch individual changes to a list of StatefulSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_replica_set_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_replica_set_list_for_all_namespaces

    watch individual changes to a list of ReplicaSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_apps_v1_stateful_set_list_for_all_namespaces(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_apps_v1_stateful_set_list_for_all_namespaces

    watch individual changes to a list of StatefulSet. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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
