# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1HostPortRange(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, max: int=None, min: int=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1HostPortRange - a model defined in Swagger

        :param max: The max of this IoK8sApiExtensionsV1beta1HostPortRange.  # noqa: E501
        :type max: int
        :param min: The min of this IoK8sApiExtensionsV1beta1HostPortRange.  # noqa: E501
        :type min: int
        """
        self.swagger_types = {
            'max': int,
            'min': int
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min'
        }

        self._max = max
        self._min = min

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1HostPortRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.HostPortRange of this IoK8sApiExtensionsV1beta1HostPortRange.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1HostPortRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max(self) -> int:
        """Gets the max of this IoK8sApiExtensionsV1beta1HostPortRange.

        max is the end of the range, inclusive.  # noqa: E501

        :return: The max of this IoK8sApiExtensionsV1beta1HostPortRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max: int):
        """Sets the max of this IoK8sApiExtensionsV1beta1HostPortRange.

        max is the end of the range, inclusive.  # noqa: E501

        :param max: The max of this IoK8sApiExtensionsV1beta1HostPortRange.
        :type max: int
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self) -> int:
        """Gets the min of this IoK8sApiExtensionsV1beta1HostPortRange.

        min is the start of the range, inclusive.  # noqa: E501

        :return: The min of this IoK8sApiExtensionsV1beta1HostPortRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min: int):
        """Sets the min of this IoK8sApiExtensionsV1beta1HostPortRange.

        min is the start of the range, inclusive.  # noqa: E501

        :param min: The min of this IoK8sApiExtensionsV1beta1HostPortRange.
        :type min: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min
