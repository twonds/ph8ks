import connexion
import six

from swagger_server.models.io_k8s_api_storage_v1beta1_csi_driver import IoK8sApiStorageV1beta1CSIDriver  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_csi_driver_list import IoK8sApiStorageV1beta1CSIDriverList  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_csi_node import IoK8sApiStorageV1beta1CSINode  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_csi_node_list import IoK8sApiStorageV1beta1CSINodeList  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_storage_class import IoK8sApiStorageV1beta1StorageClass  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_storage_class_list import IoK8sApiStorageV1beta1StorageClassList  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_volume_attachment import IoK8sApiStorageV1beta1VolumeAttachment  # noqa: E501
from swagger_server.models.io_k8s_api_storage_v1beta1_volume_attachment_list import IoK8sApiStorageV1beta1VolumeAttachmentList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_patch import IoK8sApimachineryPkgApisMetaV1Patch  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent  # noqa: E501
from swagger_server import util


def create_storage_v1beta1_csi_driver(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_storage_v1beta1_csi_driver

    create a CSIDriver # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1CSIDriver
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1CSIDriver.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_storage_v1beta1_csi_node(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_storage_v1beta1_csi_node

    create a CSINode # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1CSINode
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1CSINode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_storage_v1beta1_storage_class(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_storage_v1beta1_storage_class

    create a StorageClass # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1StorageClass
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1StorageClass.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_storage_v1beta1_volume_attachment(body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """create_storage_v1beta1_volume_attachment

    create a VolumeAttachment # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1VolumeAttachment
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1VolumeAttachment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_storage_v1beta1_collection_csi_driver(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_storage_v1beta1_collection_csi_driver

    delete collection of CSIDriver # noqa: E501

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


def delete_storage_v1beta1_collection_csi_node(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_storage_v1beta1_collection_csi_node

    delete collection of CSINode # noqa: E501

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


def delete_storage_v1beta1_collection_storage_class(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_storage_v1beta1_collection_storage_class

    delete collection of StorageClass # noqa: E501

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


def delete_storage_v1beta1_collection_volume_attachment(pretty=None, allowWatchBookmarks=None, body=None, _continue=None, dryRun=None, fieldSelector=None, gracePeriodSeconds=None, labelSelector=None, limit=None, orphanDependents=None, propagationPolicy=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """delete_storage_v1beta1_collection_volume_attachment

    delete collection of VolumeAttachment # noqa: E501

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


def delete_storage_v1beta1_csi_driver(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_storage_v1beta1_csi_driver

    delete a CSIDriver # noqa: E501

    :param name: name of the CSIDriver
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


def delete_storage_v1beta1_csi_node(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_storage_v1beta1_csi_node

    delete a CSINode # noqa: E501

    :param name: name of the CSINode
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


def delete_storage_v1beta1_storage_class(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_storage_v1beta1_storage_class

    delete a StorageClass # noqa: E501

    :param name: name of the StorageClass
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


def delete_storage_v1beta1_volume_attachment(name, pretty=None, body=None, dryRun=None, gracePeriodSeconds=None, orphanDependents=None, propagationPolicy=None):  # noqa: E501
    """delete_storage_v1beta1_volume_attachment

    delete a VolumeAttachment # noqa: E501

    :param name: name of the VolumeAttachment
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


def get_storage_v1beta1_api_resources():  # noqa: E501
    """get_storage_v1beta1_api_resources

    get available resources # noqa: E501


    :rtype: IoK8sApimachineryPkgApisMetaV1APIResourceList
    """
    return 'do some magic!'


def list_storage_v1beta1_csi_driver(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_storage_v1beta1_csi_driver

    list or watch objects of kind CSIDriver # noqa: E501

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

    :rtype: IoK8sApiStorageV1beta1CSIDriverList
    """
    return 'do some magic!'


def list_storage_v1beta1_csi_node(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_storage_v1beta1_csi_node

    list or watch objects of kind CSINode # noqa: E501

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

    :rtype: IoK8sApiStorageV1beta1CSINodeList
    """
    return 'do some magic!'


def list_storage_v1beta1_storage_class(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_storage_v1beta1_storage_class

    list or watch objects of kind StorageClass # noqa: E501

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

    :rtype: IoK8sApiStorageV1beta1StorageClassList
    """
    return 'do some magic!'


def list_storage_v1beta1_volume_attachment(pretty=None, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """list_storage_v1beta1_volume_attachment

    list or watch objects of kind VolumeAttachment # noqa: E501

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

    :rtype: IoK8sApiStorageV1beta1VolumeAttachmentList
    """
    return 'do some magic!'


def patch_storage_v1beta1_csi_driver(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_storage_v1beta1_csi_driver

    partially update the specified CSIDriver # noqa: E501

    :param name: name of the CSIDriver
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

    :rtype: IoK8sApiStorageV1beta1CSIDriver
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_storage_v1beta1_csi_node(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_storage_v1beta1_csi_node

    partially update the specified CSINode # noqa: E501

    :param name: name of the CSINode
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

    :rtype: IoK8sApiStorageV1beta1CSINode
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_storage_v1beta1_storage_class(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_storage_v1beta1_storage_class

    partially update the specified StorageClass # noqa: E501

    :param name: name of the StorageClass
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

    :rtype: IoK8sApiStorageV1beta1StorageClass
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_storage_v1beta1_volume_attachment(name, body, pretty=None, dryRun=None, fieldManager=None, force=None):  # noqa: E501
    """patch_storage_v1beta1_volume_attachment

    partially update the specified VolumeAttachment # noqa: E501

    :param name: name of the VolumeAttachment
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

    :rtype: IoK8sApiStorageV1beta1VolumeAttachment
    """
    if connexion.request.is_json:
        body = IoK8sApimachineryPkgApisMetaV1Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def read_storage_v1beta1_csi_driver(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_storage_v1beta1_csi_driver

    read the specified CSIDriver # noqa: E501

    :param name: name of the CSIDriver
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiStorageV1beta1CSIDriver
    """
    return 'do some magic!'


def read_storage_v1beta1_csi_node(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_storage_v1beta1_csi_node

    read the specified CSINode # noqa: E501

    :param name: name of the CSINode
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiStorageV1beta1CSINode
    """
    return 'do some magic!'


def read_storage_v1beta1_storage_class(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_storage_v1beta1_storage_class

    read the specified StorageClass # noqa: E501

    :param name: name of the StorageClass
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiStorageV1beta1StorageClass
    """
    return 'do some magic!'


def read_storage_v1beta1_volume_attachment(name, pretty=None, exact=None, export=None):  # noqa: E501
    """read_storage_v1beta1_volume_attachment

    read the specified VolumeAttachment # noqa: E501

    :param name: name of the VolumeAttachment
    :type name: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param exact: Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18.
    :type exact: bool
    :param export: Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18.
    :type export: bool

    :rtype: IoK8sApiStorageV1beta1VolumeAttachment
    """
    return 'do some magic!'


def replace_storage_v1beta1_csi_driver(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_storage_v1beta1_csi_driver

    replace the specified CSIDriver # noqa: E501

    :param name: name of the CSIDriver
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1CSIDriver
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1CSIDriver.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_storage_v1beta1_csi_node(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_storage_v1beta1_csi_node

    replace the specified CSINode # noqa: E501

    :param name: name of the CSINode
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1CSINode
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1CSINode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_storage_v1beta1_storage_class(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_storage_v1beta1_storage_class

    replace the specified StorageClass # noqa: E501

    :param name: name of the StorageClass
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1StorageClass
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1StorageClass.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def replace_storage_v1beta1_volume_attachment(name, body, pretty=None, dryRun=None, fieldManager=None):  # noqa: E501
    """replace_storage_v1beta1_volume_attachment

    replace the specified VolumeAttachment # noqa: E501

    :param name: name of the VolumeAttachment
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str

    :rtype: IoK8sApiStorageV1beta1VolumeAttachment
    """
    if connexion.request.is_json:
        body = IoK8sApiStorageV1beta1VolumeAttachment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def watch_storage_v1beta1_csi_driver(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_csi_driver

    watch changes to an object of kind CSIDriver. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the CSIDriver
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


def watch_storage_v1beta1_csi_driver_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_csi_driver_list

    watch individual changes to a list of CSIDriver. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_storage_v1beta1_csi_node(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_csi_node

    watch changes to an object of kind CSINode. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the CSINode
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


def watch_storage_v1beta1_csi_node_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_csi_node_list

    watch individual changes to a list of CSINode. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_storage_v1beta1_storage_class(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_storage_class

    watch changes to an object of kind StorageClass. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the StorageClass
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


def watch_storage_v1beta1_storage_class_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_storage_class_list

    watch individual changes to a list of StorageClass. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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


def watch_storage_v1beta1_volume_attachment(name, allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_volume_attachment

    watch changes to an object of kind VolumeAttachment. deprecated: use the &#39;watch&#39; parameter with a list operation instead, filtered to a single item with the &#39;fieldSelector&#39; parameter. # noqa: E501

    :param name: name of the VolumeAttachment
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


def watch_storage_v1beta1_volume_attachment_list(allowWatchBookmarks=None, _continue=None, fieldSelector=None, labelSelector=None, limit=None, pretty=None, resourceVersion=None, timeoutSeconds=None, watch=None):  # noqa: E501
    """watch_storage_v1beta1_volume_attachment_list

    watch individual changes to a list of VolumeAttachment. deprecated: use the &#39;watch&#39; parameter with a list operation instead. # noqa: E501

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
