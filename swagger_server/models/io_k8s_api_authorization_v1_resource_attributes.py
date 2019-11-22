# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthorizationV1ResourceAttributes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, group: str=None, name: str=None, namespace: str=None, resource: str=None, subresource: str=None, verb: str=None, version: str=None):  # noqa: E501
        """IoK8sApiAuthorizationV1ResourceAttributes - a model defined in Swagger

        :param group: The group of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type group: str
        :param name: The name of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type name: str
        :param namespace: The namespace of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type namespace: str
        :param resource: The resource of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type resource: str
        :param subresource: The subresource of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type subresource: str
        :param verb: The verb of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type verb: str
        :param version: The version of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'group': str,
            'name': str,
            'namespace': str,
            'resource': str,
            'subresource': str,
            'verb': str,
            'version': str
        }

        self.attribute_map = {
            'group': 'group',
            'name': 'name',
            'namespace': 'namespace',
            'resource': 'resource',
            'subresource': 'subresource',
            'verb': 'verb',
            'version': 'version'
        }

        self._group = group
        self._name = name
        self._namespace = namespace
        self._resource = resource
        self._subresource = subresource
        self._verb = verb
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthorizationV1ResourceAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authorization.v1.ResourceAttributes of this IoK8sApiAuthorizationV1ResourceAttributes.  # noqa: E501
        :rtype: IoK8sApiAuthorizationV1ResourceAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group(self) -> str:
        """Gets the group of this IoK8sApiAuthorizationV1ResourceAttributes.

        Group is the API Group of the Resource.  \"*\" means all.  # noqa: E501

        :return: The group of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this IoK8sApiAuthorizationV1ResourceAttributes.

        Group is the API Group of the Resource.  \"*\" means all.  # noqa: E501

        :param group: The group of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type group: str
        """

        self._group = group

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApiAuthorizationV1ResourceAttributes.

        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.  # noqa: E501

        :return: The name of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApiAuthorizationV1ResourceAttributes.

        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.  # noqa: E501

        :param name: The name of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type name: str
        """

        self._name = name

    @property
    def namespace(self) -> str:
        """Gets the namespace of this IoK8sApiAuthorizationV1ResourceAttributes.

        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview  # noqa: E501

        :return: The namespace of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this IoK8sApiAuthorizationV1ResourceAttributes.

        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview  # noqa: E501

        :param namespace: The namespace of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def resource(self) -> str:
        """Gets the resource of this IoK8sApiAuthorizationV1ResourceAttributes.

        Resource is one of the existing resource types.  \"*\" means all.  # noqa: E501

        :return: The resource of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str):
        """Sets the resource of this IoK8sApiAuthorizationV1ResourceAttributes.

        Resource is one of the existing resource types.  \"*\" means all.  # noqa: E501

        :param resource: The resource of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type resource: str
        """

        self._resource = resource

    @property
    def subresource(self) -> str:
        """Gets the subresource of this IoK8sApiAuthorizationV1ResourceAttributes.

        Subresource is one of the existing resource types.  \"\" means none.  # noqa: E501

        :return: The subresource of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._subresource

    @subresource.setter
    def subresource(self, subresource: str):
        """Sets the subresource of this IoK8sApiAuthorizationV1ResourceAttributes.

        Subresource is one of the existing resource types.  \"\" means none.  # noqa: E501

        :param subresource: The subresource of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type subresource: str
        """

        self._subresource = subresource

    @property
    def verb(self) -> str:
        """Gets the verb of this IoK8sApiAuthorizationV1ResourceAttributes.

        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :return: The verb of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb: str):
        """Sets the verb of this IoK8sApiAuthorizationV1ResourceAttributes.

        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :param verb: The verb of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type verb: str
        """

        self._verb = verb

    @property
    def version(self) -> str:
        """Gets the version of this IoK8sApiAuthorizationV1ResourceAttributes.

        Version is the API Version of the Resource.  \"*\" means all.  # noqa: E501

        :return: The version of this IoK8sApiAuthorizationV1ResourceAttributes.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this IoK8sApiAuthorizationV1ResourceAttributes.

        Version is the API Version of the Resource.  \"*\" means all.  # noqa: E501

        :param version: The version of this IoK8sApiAuthorizationV1ResourceAttributes.
        :type version: str
        """

        self._version = version
