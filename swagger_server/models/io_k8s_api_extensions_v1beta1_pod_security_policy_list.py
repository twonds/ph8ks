# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1PodSecurityPolicyList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, items: List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ListMeta=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1PodSecurityPolicyList - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.  # noqa: E501
        :type api_version: str
        :param items: The items of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.  # noqa: E501
        :type items: List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]
        :param kind: The kind of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ListMeta
        """
        self.swagger_types = {
            'api_version': str,
            'items': List[IoK8sApiExtensionsV1beta1PodSecurityPolicy],
            'kind': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ListMeta
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'items': 'items',
            'kind': 'kind',
            'metadata': 'metadata'
        }

        self._api_version = api_version
        self._items = items
        self._kind = kind
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1PodSecurityPolicyList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.PodSecurityPolicyList of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1PodSecurityPolicyList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def items(self) -> List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]:
        """Gets the items of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        items is a list of schema objects.  # noqa: E501

        :return: The items of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :rtype: List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]
        """
        return self._items

    @items.setter
    def items(self, items: List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]):
        """Sets the items of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        items is a list of schema objects.  # noqa: E501

        :param items: The items of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :type items: List[IoK8sApiExtensionsV1beta1PodSecurityPolicy]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ListMeta:
        """Gets the metadata of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :rtype: IoK8sApimachineryPkgApisMetaV1ListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ListMeta):
        """Sets the metadata of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.

        Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiExtensionsV1beta1PodSecurityPolicyList.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ListMeta
        """

        self._metadata = metadata