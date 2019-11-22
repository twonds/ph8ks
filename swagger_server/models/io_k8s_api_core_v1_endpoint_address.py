# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1EndpointAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hostname: str=None, ip: str=None, node_name: str=None, target_ref: IoK8sApiCoreV1ObjectReference=None):  # noqa: E501
        """IoK8sApiCoreV1EndpointAddress - a model defined in Swagger

        :param hostname: The hostname of this IoK8sApiCoreV1EndpointAddress.  # noqa: E501
        :type hostname: str
        :param ip: The ip of this IoK8sApiCoreV1EndpointAddress.  # noqa: E501
        :type ip: str
        :param node_name: The node_name of this IoK8sApiCoreV1EndpointAddress.  # noqa: E501
        :type node_name: str
        :param target_ref: The target_ref of this IoK8sApiCoreV1EndpointAddress.  # noqa: E501
        :type target_ref: IoK8sApiCoreV1ObjectReference
        """
        self.swagger_types = {
            'hostname': str,
            'ip': str,
            'node_name': str,
            'target_ref': IoK8sApiCoreV1ObjectReference
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'ip': 'ip',
            'node_name': 'nodeName',
            'target_ref': 'targetRef'
        }

        self._hostname = hostname
        self._ip = ip
        self._node_name = node_name
        self._target_ref = target_ref

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1EndpointAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.EndpointAddress of this IoK8sApiCoreV1EndpointAddress.  # noqa: E501
        :rtype: IoK8sApiCoreV1EndpointAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hostname(self) -> str:
        """Gets the hostname of this IoK8sApiCoreV1EndpointAddress.

        The Hostname of this endpoint  # noqa: E501

        :return: The hostname of this IoK8sApiCoreV1EndpointAddress.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """Sets the hostname of this IoK8sApiCoreV1EndpointAddress.

        The Hostname of this endpoint  # noqa: E501

        :param hostname: The hostname of this IoK8sApiCoreV1EndpointAddress.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def ip(self) -> str:
        """Gets the ip of this IoK8sApiCoreV1EndpointAddress.

        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.  # noqa: E501

        :return: The ip of this IoK8sApiCoreV1EndpointAddress.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this IoK8sApiCoreV1EndpointAddress.

        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.  # noqa: E501

        :param ip: The ip of this IoK8sApiCoreV1EndpointAddress.
        :type ip: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def node_name(self) -> str:
        """Gets the node_name of this IoK8sApiCoreV1EndpointAddress.

        Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.  # noqa: E501

        :return: The node_name of this IoK8sApiCoreV1EndpointAddress.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name: str):
        """Sets the node_name of this IoK8sApiCoreV1EndpointAddress.

        Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.  # noqa: E501

        :param node_name: The node_name of this IoK8sApiCoreV1EndpointAddress.
        :type node_name: str
        """

        self._node_name = node_name

    @property
    def target_ref(self) -> IoK8sApiCoreV1ObjectReference:
        """Gets the target_ref of this IoK8sApiCoreV1EndpointAddress.

        Reference to object providing the endpoint.  # noqa: E501

        :return: The target_ref of this IoK8sApiCoreV1EndpointAddress.
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref: IoK8sApiCoreV1ObjectReference):
        """Sets the target_ref of this IoK8sApiCoreV1EndpointAddress.

        Reference to object providing the endpoint.  # noqa: E501

        :param target_ref: The target_ref of this IoK8sApiCoreV1EndpointAddress.
        :type target_ref: IoK8sApiCoreV1ObjectReference
        """

        self._target_ref = target_ref
