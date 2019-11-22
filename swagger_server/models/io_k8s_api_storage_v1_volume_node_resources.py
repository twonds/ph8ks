# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiStorageV1VolumeNodeResources(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None):  # noqa: E501
        """IoK8sApiStorageV1VolumeNodeResources - a model defined in Swagger

        :param count: The count of this IoK8sApiStorageV1VolumeNodeResources.  # noqa: E501
        :type count: int
        """
        self.swagger_types = {
            'count': int
        }

        self.attribute_map = {
            'count': 'count'
        }

        self._count = count

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiStorageV1VolumeNodeResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.storage.v1.VolumeNodeResources of this IoK8sApiStorageV1VolumeNodeResources.  # noqa: E501
        :rtype: IoK8sApiStorageV1VolumeNodeResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this IoK8sApiStorageV1VolumeNodeResources.

        Maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.  # noqa: E501

        :return: The count of this IoK8sApiStorageV1VolumeNodeResources.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this IoK8sApiStorageV1VolumeNodeResources.

        Maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.  # noqa: E501

        :param count: The count of this IoK8sApiStorageV1VolumeNodeResources.
        :type count: int
        """

        self._count = count
