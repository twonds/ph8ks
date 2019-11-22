# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1Capabilities(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, add: List[str]=None, drop: List[str]=None):  # noqa: E501
        """IoK8sApiCoreV1Capabilities - a model defined in Swagger

        :param add: The add of this IoK8sApiCoreV1Capabilities.  # noqa: E501
        :type add: List[str]
        :param drop: The drop of this IoK8sApiCoreV1Capabilities.  # noqa: E501
        :type drop: List[str]
        """
        self.swagger_types = {
            'add': List[str],
            'drop': List[str]
        }

        self.attribute_map = {
            'add': 'add',
            'drop': 'drop'
        }

        self._add = add
        self._drop = drop

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1Capabilities':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.Capabilities of this IoK8sApiCoreV1Capabilities.  # noqa: E501
        :rtype: IoK8sApiCoreV1Capabilities
        """
        return util.deserialize_model(dikt, cls)

    @property
    def add(self) -> List[str]:
        """Gets the add of this IoK8sApiCoreV1Capabilities.

        Added capabilities  # noqa: E501

        :return: The add of this IoK8sApiCoreV1Capabilities.
        :rtype: List[str]
        """
        return self._add

    @add.setter
    def add(self, add: List[str]):
        """Sets the add of this IoK8sApiCoreV1Capabilities.

        Added capabilities  # noqa: E501

        :param add: The add of this IoK8sApiCoreV1Capabilities.
        :type add: List[str]
        """

        self._add = add

    @property
    def drop(self) -> List[str]:
        """Gets the drop of this IoK8sApiCoreV1Capabilities.

        Removed capabilities  # noqa: E501

        :return: The drop of this IoK8sApiCoreV1Capabilities.
        :rtype: List[str]
        """
        return self._drop

    @drop.setter
    def drop(self, drop: List[str]):
        """Sets the drop of this IoK8sApiCoreV1Capabilities.

        Removed capabilities  # noqa: E501

        :param drop: The drop of this IoK8sApiCoreV1Capabilities.
        :type drop: List[str]
        """

        self._drop = drop
