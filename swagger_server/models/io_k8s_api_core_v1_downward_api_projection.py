# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1DownwardAPIProjection(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, items: List[IoK8sApiCoreV1DownwardAPIVolumeFile]=None):  # noqa: E501
        """IoK8sApiCoreV1DownwardAPIProjection - a model defined in Swagger

        :param items: The items of this IoK8sApiCoreV1DownwardAPIProjection.  # noqa: E501
        :type items: List[IoK8sApiCoreV1DownwardAPIVolumeFile]
        """
        self.swagger_types = {
            'items': List[IoK8sApiCoreV1DownwardAPIVolumeFile]
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1DownwardAPIProjection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.DownwardAPIProjection of this IoK8sApiCoreV1DownwardAPIProjection.  # noqa: E501
        :rtype: IoK8sApiCoreV1DownwardAPIProjection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[IoK8sApiCoreV1DownwardAPIVolumeFile]:
        """Gets the items of this IoK8sApiCoreV1DownwardAPIProjection.

        Items is a list of DownwardAPIVolume file  # noqa: E501

        :return: The items of this IoK8sApiCoreV1DownwardAPIProjection.
        :rtype: List[IoK8sApiCoreV1DownwardAPIVolumeFile]
        """
        return self._items

    @items.setter
    def items(self, items: List[IoK8sApiCoreV1DownwardAPIVolumeFile]):
        """Sets the items of this IoK8sApiCoreV1DownwardAPIProjection.

        Items is a list of DownwardAPIVolume file  # noqa: E501

        :param items: The items of this IoK8sApiCoreV1DownwardAPIProjection.
        :type items: List[IoK8sApiCoreV1DownwardAPIVolumeFile]
        """

        self._items = items
