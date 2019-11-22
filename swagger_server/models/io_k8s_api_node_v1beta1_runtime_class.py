# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiNodeV1beta1RuntimeClass(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, handler: str=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, overhead: IoK8sApiNodeV1beta1Overhead=None, scheduling: IoK8sApiNodeV1beta1Scheduling=None):  # noqa: E501
        """IoK8sApiNodeV1beta1RuntimeClass - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type api_version: str
        :param handler: The handler of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type handler: str
        :param kind: The kind of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param overhead: The overhead of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type overhead: IoK8sApiNodeV1beta1Overhead
        :param scheduling: The scheduling of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :type scheduling: IoK8sApiNodeV1beta1Scheduling
        """
        self.swagger_types = {
            'api_version': str,
            'handler': str,
            'kind': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'overhead': IoK8sApiNodeV1beta1Overhead,
            'scheduling': IoK8sApiNodeV1beta1Scheduling
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'handler': 'handler',
            'kind': 'kind',
            'metadata': 'metadata',
            'overhead': 'overhead',
            'scheduling': 'scheduling'
        }

        self._api_version = api_version
        self._handler = handler
        self._kind = kind
        self._metadata = metadata
        self._overhead = overhead
        self._scheduling = scheduling

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiNodeV1beta1RuntimeClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.node.v1beta1.RuntimeClass of this IoK8sApiNodeV1beta1RuntimeClass.  # noqa: E501
        :rtype: IoK8sApiNodeV1beta1RuntimeClass
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiNodeV1beta1RuntimeClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiNodeV1beta1RuntimeClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiNodeV1beta1RuntimeClass.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def handler(self) -> str:
        """Gets the handler of this IoK8sApiNodeV1beta1RuntimeClass.

        Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :return: The handler of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler: str):
        """Sets the handler of this IoK8sApiNodeV1beta1RuntimeClass.

        Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :param handler: The handler of this IoK8sApiNodeV1beta1RuntimeClass.
        :type handler: str
        """
        if handler is None:
            raise ValueError("Invalid value for `handler`, must not be `None`")  # noqa: E501

        self._handler = handler

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiNodeV1beta1RuntimeClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiNodeV1beta1RuntimeClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiNodeV1beta1RuntimeClass.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiNodeV1beta1RuntimeClass.

        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiNodeV1beta1RuntimeClass.

        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiNodeV1beta1RuntimeClass.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def overhead(self) -> IoK8sApiNodeV1beta1Overhead:
        """Gets the overhead of this IoK8sApiNodeV1beta1RuntimeClass.

        Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.  # noqa: E501

        :return: The overhead of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: IoK8sApiNodeV1beta1Overhead
        """
        return self._overhead

    @overhead.setter
    def overhead(self, overhead: IoK8sApiNodeV1beta1Overhead):
        """Sets the overhead of this IoK8sApiNodeV1beta1RuntimeClass.

        Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.  # noqa: E501

        :param overhead: The overhead of this IoK8sApiNodeV1beta1RuntimeClass.
        :type overhead: IoK8sApiNodeV1beta1Overhead
        """

        self._overhead = overhead

    @property
    def scheduling(self) -> IoK8sApiNodeV1beta1Scheduling:
        """Gets the scheduling of this IoK8sApiNodeV1beta1RuntimeClass.

        Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.  # noqa: E501

        :return: The scheduling of this IoK8sApiNodeV1beta1RuntimeClass.
        :rtype: IoK8sApiNodeV1beta1Scheduling
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling: IoK8sApiNodeV1beta1Scheduling):
        """Sets the scheduling of this IoK8sApiNodeV1beta1RuntimeClass.

        Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.  # noqa: E501

        :param scheduling: The scheduling of this IoK8sApiNodeV1beta1RuntimeClass.
        :type scheduling: IoK8sApiNodeV1beta1Scheduling
        """

        self._scheduling = scheduling
