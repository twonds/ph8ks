# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1EmptyDirVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, medium: str=None, size_limit: IoK8sApimachineryPkgApiResourceQuantity=None):  # noqa: E501
        """IoK8sApiCoreV1EmptyDirVolumeSource - a model defined in Swagger

        :param medium: The medium of this IoK8sApiCoreV1EmptyDirVolumeSource.  # noqa: E501
        :type medium: str
        :param size_limit: The size_limit of this IoK8sApiCoreV1EmptyDirVolumeSource.  # noqa: E501
        :type size_limit: IoK8sApimachineryPkgApiResourceQuantity
        """
        self.swagger_types = {
            'medium': str,
            'size_limit': IoK8sApimachineryPkgApiResourceQuantity
        }

        self.attribute_map = {
            'medium': 'medium',
            'size_limit': 'sizeLimit'
        }

        self._medium = medium
        self._size_limit = size_limit

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1EmptyDirVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.EmptyDirVolumeSource of this IoK8sApiCoreV1EmptyDirVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1EmptyDirVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def medium(self) -> str:
        """Gets the medium of this IoK8sApiCoreV1EmptyDirVolumeSource.

        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir  # noqa: E501

        :return: The medium of this IoK8sApiCoreV1EmptyDirVolumeSource.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium: str):
        """Sets the medium of this IoK8sApiCoreV1EmptyDirVolumeSource.

        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir  # noqa: E501

        :param medium: The medium of this IoK8sApiCoreV1EmptyDirVolumeSource.
        :type medium: str
        """

        self._medium = medium

    @property
    def size_limit(self) -> IoK8sApimachineryPkgApiResourceQuantity:
        """Gets the size_limit of this IoK8sApiCoreV1EmptyDirVolumeSource.

        Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir  # noqa: E501

        :return: The size_limit of this IoK8sApiCoreV1EmptyDirVolumeSource.
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._size_limit

    @size_limit.setter
    def size_limit(self, size_limit: IoK8sApimachineryPkgApiResourceQuantity):
        """Sets the size_limit of this IoK8sApiCoreV1EmptyDirVolumeSource.

        Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir  # noqa: E501

        :param size_limit: The size_limit of this IoK8sApiCoreV1EmptyDirVolumeSource.
        :type size_limit: IoK8sApimachineryPkgApiResourceQuantity
        """

        self._size_limit = size_limit
