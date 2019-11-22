# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAdmissionregistrationV1RuleWithOperations(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_groups: List[str]=None, api_versions: List[str]=None, operations: List[str]=None, resources: List[str]=None, scope: str=None):  # noqa: E501
        """IoK8sApiAdmissionregistrationV1RuleWithOperations - a model defined in Swagger

        :param api_groups: The api_groups of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :type api_groups: List[str]
        :param api_versions: The api_versions of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :type api_versions: List[str]
        :param operations: The operations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :type operations: List[str]
        :param resources: The resources of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :type resources: List[str]
        :param scope: The scope of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :type scope: str
        """
        self.swagger_types = {
            'api_groups': List[str],
            'api_versions': List[str],
            'operations': List[str],
            'resources': List[str],
            'scope': str
        }

        self.attribute_map = {
            'api_groups': 'apiGroups',
            'api_versions': 'apiVersions',
            'operations': 'operations',
            'resources': 'resources',
            'scope': 'scope'
        }

        self._api_groups = api_groups
        self._api_versions = api_versions
        self._operations = operations
        self._resources = resources
        self._scope = scope

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAdmissionregistrationV1RuleWithOperations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.admissionregistration.v1.RuleWithOperations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.  # noqa: E501
        :rtype: IoK8sApiAdmissionregistrationV1RuleWithOperations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_groups(self) -> List[str]:
        """Gets the api_groups of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :return: The api_groups of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :rtype: List[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups: List[str]):
        """Sets the api_groups of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :param api_groups: The api_groups of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :type api_groups: List[str]
        """

        self._api_groups = api_groups

    @property
    def api_versions(self) -> List[str]:
        """Gets the api_versions of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :return: The api_versions of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :rtype: List[str]
        """
        return self._api_versions

    @api_versions.setter
    def api_versions(self, api_versions: List[str]):
        """Sets the api_versions of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :param api_versions: The api_versions of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :type api_versions: List[str]
        """

        self._api_versions = api_versions

    @property
    def operations(self) -> List[str]:
        """Gets the operations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all operations. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :return: The operations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :rtype: List[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations: List[str]):
        """Sets the operations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all operations. If '*' is present, the length of the slice must be one. Required.  # noqa: E501

        :param operations: The operations of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :type operations: List[str]
        """

        self._operations = operations

    @property
    def resources(self) -> List[str]:
        """Gets the resources of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.  # noqa: E501

        :return: The resources of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :rtype: List[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources: List[str]):
        """Sets the resources of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.  # noqa: E501

        :param resources: The resources of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :type resources: List[str]
        """

        self._resources = resources

    @property
    def scope(self) -> str:
        """Gets the scope of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        scope specifies the scope of this rule. Valid values are \"Cluster\", \"Namespaced\", and \"*\" \"Cluster\" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \"Namespaced\" means that only namespaced resources will match this rule. \"*\" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \"*\".  # noqa: E501

        :return: The scope of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope: str):
        """Sets the scope of this IoK8sApiAdmissionregistrationV1RuleWithOperations.

        scope specifies the scope of this rule. Valid values are \"Cluster\", \"Namespaced\", and \"*\" \"Cluster\" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \"Namespaced\" means that only namespaced resources will match this rule. \"*\" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \"*\".  # noqa: E501

        :param scope: The scope of this IoK8sApiAdmissionregistrationV1RuleWithOperations.
        :type scope: str
        """

        self._scope = scope
