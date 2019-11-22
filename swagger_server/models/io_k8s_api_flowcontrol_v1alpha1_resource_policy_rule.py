# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_groups: List[str]=None, cluster_scope: bool=None, namespaces: List[str]=None, resources: List[str]=None, verbs: List[str]=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule - a model defined in Swagger

        :param api_groups: The api_groups of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :type api_groups: List[str]
        :param cluster_scope: The cluster_scope of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :type cluster_scope: bool
        :param namespaces: The namespaces of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :type namespaces: List[str]
        :param resources: The resources of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :type resources: List[str]
        :param verbs: The verbs of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :type verbs: List[str]
        """
        self.swagger_types = {
            'api_groups': List[str],
            'cluster_scope': bool,
            'namespaces': List[str],
            'resources': List[str],
            'verbs': List[str]
        }

        self.attribute_map = {
            'api_groups': 'apiGroups',
            'cluster_scope': 'clusterScope',
            'namespaces': 'namespaces',
            'resources': 'resources',
            'verbs': 'verbs'
        }

        self._api_groups = api_groups
        self._cluster_scope = cluster_scope
        self._namespaces = namespaces
        self._resources = resources
        self._verbs = verbs

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.flowcontrol.v1alpha1.ResourcePolicyRule of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_groups(self) -> List[str]:
        """Gets the api_groups of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `apiGroups` is a list of matching API groups and may not be empty. \"*\" matches all API groups and, if present, must be the only entry. Required.  # noqa: E501

        :return: The api_groups of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :rtype: List[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups: List[str]):
        """Sets the api_groups of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `apiGroups` is a list of matching API groups and may not be empty. \"*\" matches all API groups and, if present, must be the only entry. Required.  # noqa: E501

        :param api_groups: The api_groups of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :type api_groups: List[str]
        """
        if api_groups is None:
            raise ValueError("Invalid value for `api_groups`, must not be `None`")  # noqa: E501

        self._api_groups = api_groups

    @property
    def cluster_scope(self) -> bool:
        """Gets the cluster_scope of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.  # noqa: E501

        :return: The cluster_scope of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :rtype: bool
        """
        return self._cluster_scope

    @cluster_scope.setter
    def cluster_scope(self, cluster_scope: bool):
        """Sets the cluster_scope of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.  # noqa: E501

        :param cluster_scope: The cluster_scope of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :type cluster_scope: bool
        """

        self._cluster_scope = cluster_scope

    @property
    def namespaces(self) -> List[str]:
        """Gets the namespaces of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains \"*\".  Note that \"*\" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.  # noqa: E501

        :return: The namespaces of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :rtype: List[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces: List[str]):
        """Sets the namespaces of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains \"*\".  Note that \"*\" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.  # noqa: E501

        :param namespaces: The namespaces of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :type namespaces: List[str]
        """

        self._namespaces = namespaces

    @property
    def resources(self) -> List[str]:
        """Gets the resources of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ \"services\", \"nodes/status\" ].  This list may not be empty. \"*\" matches all resources and, if present, must be the only entry. Required.  # noqa: E501

        :return: The resources of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :rtype: List[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources: List[str]):
        """Sets the resources of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ \"services\", \"nodes/status\" ].  This list may not be empty. \"*\" matches all resources and, if present, must be the only entry. Required.  # noqa: E501

        :param resources: The resources of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :type resources: List[str]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def verbs(self) -> List[str]:
        """Gets the verbs of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs and, if present, must be the only entry. Required.  # noqa: E501

        :return: The verbs of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :rtype: List[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs: List[str]):
        """Sets the verbs of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs and, if present, must be the only entry. Required.  # noqa: E501

        :param verbs: The verbs of this IoK8sApiFlowcontrolV1alpha1ResourcePolicyRule.
        :type verbs: List[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs