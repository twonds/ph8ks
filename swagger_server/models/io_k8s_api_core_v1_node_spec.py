# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1NodeSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, config_source: IoK8sApiCoreV1NodeConfigSource=None, external_id: str=None, pod_cidr: str=None, pod_cid_rs: List[str]=None, provider_id: str=None, taints: List[IoK8sApiCoreV1Taint]=None, unschedulable: bool=None):  # noqa: E501
        """IoK8sApiCoreV1NodeSpec - a model defined in Swagger

        :param config_source: The config_source of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type config_source: IoK8sApiCoreV1NodeConfigSource
        :param external_id: The external_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type external_id: str
        :param pod_cidr: The pod_cidr of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type pod_cidr: str
        :param pod_cid_rs: The pod_cid_rs of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type pod_cid_rs: List[str]
        :param provider_id: The provider_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type provider_id: str
        :param taints: The taints of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type taints: List[IoK8sApiCoreV1Taint]
        :param unschedulable: The unschedulable of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type unschedulable: bool
        """
        self.swagger_types = {
            'config_source': IoK8sApiCoreV1NodeConfigSource,
            'external_id': str,
            'pod_cidr': str,
            'pod_cid_rs': List[str],
            'provider_id': str,
            'taints': List[IoK8sApiCoreV1Taint],
            'unschedulable': bool
        }

        self.attribute_map = {
            'config_source': 'configSource',
            'external_id': 'externalID',
            'pod_cidr': 'podCIDR',
            'pod_cid_rs': 'podCIDRs',
            'provider_id': 'providerID',
            'taints': 'taints',
            'unschedulable': 'unschedulable'
        }

        self._config_source = config_source
        self._external_id = external_id
        self._pod_cidr = pod_cidr
        self._pod_cid_rs = pod_cid_rs
        self._provider_id = provider_id
        self._taints = taints
        self._unschedulable = unschedulable

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1NodeSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.NodeSpec of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1NodeSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_source(self) -> IoK8sApiCoreV1NodeConfigSource:
        """Gets the config_source of this IoK8sApiCoreV1NodeSpec.

        If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field  # noqa: E501

        :return: The config_source of this IoK8sApiCoreV1NodeSpec.
        :rtype: IoK8sApiCoreV1NodeConfigSource
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source: IoK8sApiCoreV1NodeConfigSource):
        """Sets the config_source of this IoK8sApiCoreV1NodeSpec.

        If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field  # noqa: E501

        :param config_source: The config_source of this IoK8sApiCoreV1NodeSpec.
        :type config_source: IoK8sApiCoreV1NodeConfigSource
        """

        self._config_source = config_source

    @property
    def external_id(self) -> str:
        """Gets the external_id of this IoK8sApiCoreV1NodeSpec.

        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966  # noqa: E501

        :return: The external_id of this IoK8sApiCoreV1NodeSpec.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id: str):
        """Sets the external_id of this IoK8sApiCoreV1NodeSpec.

        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966  # noqa: E501

        :param external_id: The external_id of this IoK8sApiCoreV1NodeSpec.
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def pod_cidr(self) -> str:
        """Gets the pod_cidr of this IoK8sApiCoreV1NodeSpec.

        PodCIDR represents the pod IP range assigned to the node.  # noqa: E501

        :return: The pod_cidr of this IoK8sApiCoreV1NodeSpec.
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr: str):
        """Sets the pod_cidr of this IoK8sApiCoreV1NodeSpec.

        PodCIDR represents the pod IP range assigned to the node.  # noqa: E501

        :param pod_cidr: The pod_cidr of this IoK8sApiCoreV1NodeSpec.
        :type pod_cidr: str
        """

        self._pod_cidr = pod_cidr

    @property
    def pod_cid_rs(self) -> List[str]:
        """Gets the pod_cid_rs of this IoK8sApiCoreV1NodeSpec.

        podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.  # noqa: E501

        :return: The pod_cid_rs of this IoK8sApiCoreV1NodeSpec.
        :rtype: List[str]
        """
        return self._pod_cid_rs

    @pod_cid_rs.setter
    def pod_cid_rs(self, pod_cid_rs: List[str]):
        """Sets the pod_cid_rs of this IoK8sApiCoreV1NodeSpec.

        podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.  # noqa: E501

        :param pod_cid_rs: The pod_cid_rs of this IoK8sApiCoreV1NodeSpec.
        :type pod_cid_rs: List[str]
        """

        self._pod_cid_rs = pod_cid_rs

    @property
    def provider_id(self) -> str:
        """Gets the provider_id of this IoK8sApiCoreV1NodeSpec.

        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  # noqa: E501

        :return: The provider_id of this IoK8sApiCoreV1NodeSpec.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: str):
        """Sets the provider_id of this IoK8sApiCoreV1NodeSpec.

        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  # noqa: E501

        :param provider_id: The provider_id of this IoK8sApiCoreV1NodeSpec.
        :type provider_id: str
        """

        self._provider_id = provider_id

    @property
    def taints(self) -> List[IoK8sApiCoreV1Taint]:
        """Gets the taints of this IoK8sApiCoreV1NodeSpec.

        If specified, the node's taints.  # noqa: E501

        :return: The taints of this IoK8sApiCoreV1NodeSpec.
        :rtype: List[IoK8sApiCoreV1Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints: List[IoK8sApiCoreV1Taint]):
        """Sets the taints of this IoK8sApiCoreV1NodeSpec.

        If specified, the node's taints.  # noqa: E501

        :param taints: The taints of this IoK8sApiCoreV1NodeSpec.
        :type taints: List[IoK8sApiCoreV1Taint]
        """

        self._taints = taints

    @property
    def unschedulable(self) -> bool:
        """Gets the unschedulable of this IoK8sApiCoreV1NodeSpec.

        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration  # noqa: E501

        :return: The unschedulable of this IoK8sApiCoreV1NodeSpec.
        :rtype: bool
        """
        return self._unschedulable

    @unschedulable.setter
    def unschedulable(self, unschedulable: bool):
        """Sets the unschedulable of this IoK8sApiCoreV1NodeSpec.

        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration  # noqa: E501

        :param unschedulable: The unschedulable of this IoK8sApiCoreV1NodeSpec.
        :type unschedulable: bool
        """

        self._unschedulable = unschedulable