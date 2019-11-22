# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiDiscoveryV1beta1Endpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, addresses: List[str]=None, conditions: IoK8sApiDiscoveryV1beta1EndpointConditions=None, hostname: str=None, target_ref: IoK8sApiCoreV1ObjectReference=None, topology: Dict[str, str]=None):  # noqa: E501
        """IoK8sApiDiscoveryV1beta1Endpoint - a model defined in Swagger

        :param addresses: The addresses of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :type addresses: List[str]
        :param conditions: The conditions of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :type conditions: IoK8sApiDiscoveryV1beta1EndpointConditions
        :param hostname: The hostname of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :type hostname: str
        :param target_ref: The target_ref of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :type target_ref: IoK8sApiCoreV1ObjectReference
        :param topology: The topology of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :type topology: Dict[str, str]
        """
        self.swagger_types = {
            'addresses': List[str],
            'conditions': IoK8sApiDiscoveryV1beta1EndpointConditions,
            'hostname': str,
            'target_ref': IoK8sApiCoreV1ObjectReference,
            'topology': Dict[str, str]
        }

        self.attribute_map = {
            'addresses': 'addresses',
            'conditions': 'conditions',
            'hostname': 'hostname',
            'target_ref': 'targetRef',
            'topology': 'topology'
        }

        self._addresses = addresses
        self._conditions = conditions
        self._hostname = hostname
        self._target_ref = target_ref
        self._topology = topology

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiDiscoveryV1beta1Endpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.discovery.v1beta1.Endpoint of this IoK8sApiDiscoveryV1beta1Endpoint.  # noqa: E501
        :rtype: IoK8sApiDiscoveryV1beta1Endpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def addresses(self) -> List[str]:
        """Gets the addresses of this IoK8sApiDiscoveryV1beta1Endpoint.

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.  # noqa: E501

        :return: The addresses of this IoK8sApiDiscoveryV1beta1Endpoint.
        :rtype: List[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List[str]):
        """Sets the addresses of this IoK8sApiDiscoveryV1beta1Endpoint.

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.  # noqa: E501

        :param addresses: The addresses of this IoK8sApiDiscoveryV1beta1Endpoint.
        :type addresses: List[str]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

    @property
    def conditions(self) -> IoK8sApiDiscoveryV1beta1EndpointConditions:
        """Gets the conditions of this IoK8sApiDiscoveryV1beta1Endpoint.

        conditions contains information about the current status of the endpoint.  # noqa: E501

        :return: The conditions of this IoK8sApiDiscoveryV1beta1Endpoint.
        :rtype: IoK8sApiDiscoveryV1beta1EndpointConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: IoK8sApiDiscoveryV1beta1EndpointConditions):
        """Sets the conditions of this IoK8sApiDiscoveryV1beta1Endpoint.

        conditions contains information about the current status of the endpoint.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiDiscoveryV1beta1Endpoint.
        :type conditions: IoK8sApiDiscoveryV1beta1EndpointConditions
        """

        self._conditions = conditions

    @property
    def hostname(self) -> str:
        """Gets the hostname of this IoK8sApiDiscoveryV1beta1Endpoint.

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.  # noqa: E501

        :return: The hostname of this IoK8sApiDiscoveryV1beta1Endpoint.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """Sets the hostname of this IoK8sApiDiscoveryV1beta1Endpoint.

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.  # noqa: E501

        :param hostname: The hostname of this IoK8sApiDiscoveryV1beta1Endpoint.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def target_ref(self) -> IoK8sApiCoreV1ObjectReference:
        """Gets the target_ref of this IoK8sApiDiscoveryV1beta1Endpoint.

        targetRef is a reference to a Kubernetes object that represents this endpoint.  # noqa: E501

        :return: The target_ref of this IoK8sApiDiscoveryV1beta1Endpoint.
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref: IoK8sApiCoreV1ObjectReference):
        """Sets the target_ref of this IoK8sApiDiscoveryV1beta1Endpoint.

        targetRef is a reference to a Kubernetes object that represents this endpoint.  # noqa: E501

        :param target_ref: The target_ref of this IoK8sApiDiscoveryV1beta1Endpoint.
        :type target_ref: IoK8sApiCoreV1ObjectReference
        """

        self._target_ref = target_ref

    @property
    def topology(self) -> Dict[str, str]:
        """Gets the topology of this IoK8sApiDiscoveryV1beta1Endpoint.

        topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node   where the endpoint is located. This should match the corresponding   node label. * topology.kubernetes.io/zone: the value indicates the zone where the   endpoint is located. This should match the corresponding node label. * topology.kubernetes.io/region: the value indicates the region where the   endpoint is located. This should match the corresponding node label.  # noqa: E501

        :return: The topology of this IoK8sApiDiscoveryV1beta1Endpoint.
        :rtype: Dict[str, str]
        """
        return self._topology

    @topology.setter
    def topology(self, topology: Dict[str, str]):
        """Sets the topology of this IoK8sApiDiscoveryV1beta1Endpoint.

        topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node   where the endpoint is located. This should match the corresponding   node label. * topology.kubernetes.io/zone: the value indicates the zone where the   endpoint is located. This should match the corresponding node label. * topology.kubernetes.io/region: the value indicates the region where the   endpoint is located. This should match the corresponding node label.  # noqa: E501

        :param topology: The topology of this IoK8sApiDiscoveryV1beta1Endpoint.
        :type topology: Dict[str, str]
        """

        self._topology = topology
