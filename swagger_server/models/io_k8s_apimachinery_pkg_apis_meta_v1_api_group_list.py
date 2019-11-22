# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApimachineryPkgApisMetaV1APIGroupList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, groups: List[IoK8sApimachineryPkgApisMetaV1APIGroup]=None, kind: str=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1APIGroupList - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApimachineryPkgApisMetaV1APIGroupList.  # noqa: E501
        :type api_version: str
        :param groups: The groups of this IoK8sApimachineryPkgApisMetaV1APIGroupList.  # noqa: E501
        :type groups: List[IoK8sApimachineryPkgApisMetaV1APIGroup]
        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1APIGroupList.  # noqa: E501
        :type kind: str
        """
        self.swagger_types = {
            'api_version': str,
            'groups': List[IoK8sApimachineryPkgApisMetaV1APIGroup],
            'kind': str
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'groups': 'groups',
            'kind': 'kind'
        }

        self._api_version = api_version
        self._groups = groups
        self._kind = kind

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApimachineryPkgApisMetaV1APIGroupList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.apimachinery.pkg.apis.meta.v1.APIGroupList of this IoK8sApimachineryPkgApisMetaV1APIGroupList.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1APIGroupList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def groups(self) -> List[IoK8sApimachineryPkgApisMetaV1APIGroup]:
        """Gets the groups of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        groups is a list of APIGroup.  # noqa: E501

        :return: The groups of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :rtype: List[IoK8sApimachineryPkgApisMetaV1APIGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: List[IoK8sApimachineryPkgApisMetaV1APIGroup]):
        """Sets the groups of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        groups is a list of APIGroup.  # noqa: E501

        :param groups: The groups of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :type groups: List[IoK8sApimachineryPkgApisMetaV1APIGroup]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApimachineryPkgApisMetaV1APIGroupList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1APIGroupList.
        :type kind: str
        """

        self._kind = kind
