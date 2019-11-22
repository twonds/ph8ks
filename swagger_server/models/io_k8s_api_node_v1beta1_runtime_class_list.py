# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiNodeV1beta1RuntimeClassList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, items: List[IoK8sApiNodeV1beta1RuntimeClass]=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ListMeta=None):  # noqa: E501
        """IoK8sApiNodeV1beta1RuntimeClassList - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiNodeV1beta1RuntimeClassList.  # noqa: E501
        :type api_version: str
        :param items: The items of this IoK8sApiNodeV1beta1RuntimeClassList.  # noqa: E501
        :type items: List[IoK8sApiNodeV1beta1RuntimeClass]
        :param kind: The kind of this IoK8sApiNodeV1beta1RuntimeClassList.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiNodeV1beta1RuntimeClassList.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ListMeta
        """
        self.swagger_types = {
            'api_version': str,
            'items': List[IoK8sApiNodeV1beta1RuntimeClass],
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
    def from_dict(cls, dikt) -> 'IoK8sApiNodeV1beta1RuntimeClassList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.node.v1beta1.RuntimeClassList of this IoK8sApiNodeV1beta1RuntimeClassList.  # noqa: E501
        :rtype: IoK8sApiNodeV1beta1RuntimeClassList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiNodeV1beta1RuntimeClassList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiNodeV1beta1RuntimeClassList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiNodeV1beta1RuntimeClassList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiNodeV1beta1RuntimeClassList.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def items(self) -> List[IoK8sApiNodeV1beta1RuntimeClass]:
        """Gets the items of this IoK8sApiNodeV1beta1RuntimeClassList.

        Items is a list of schema objects.  # noqa: E501

        :return: The items of this IoK8sApiNodeV1beta1RuntimeClassList.
        :rtype: List[IoK8sApiNodeV1beta1RuntimeClass]
        """
        return self._items

    @items.setter
    def items(self, items: List[IoK8sApiNodeV1beta1RuntimeClass]):
        """Sets the items of this IoK8sApiNodeV1beta1RuntimeClassList.

        Items is a list of schema objects.  # noqa: E501

        :param items: The items of this IoK8sApiNodeV1beta1RuntimeClassList.
        :type items: List[IoK8sApiNodeV1beta1RuntimeClass]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiNodeV1beta1RuntimeClassList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiNodeV1beta1RuntimeClassList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiNodeV1beta1RuntimeClassList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiNodeV1beta1RuntimeClassList.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ListMeta:
        """Gets the metadata of this IoK8sApiNodeV1beta1RuntimeClassList.

        Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiNodeV1beta1RuntimeClassList.
        :rtype: IoK8sApimachineryPkgApisMetaV1ListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ListMeta):
        """Sets the metadata of this IoK8sApiNodeV1beta1RuntimeClassList.

        Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiNodeV1beta1RuntimeClassList.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ListMeta
        """

        self._metadata = metadata
