# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1ResourceFieldSelector(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, container_name: str=None, divisor: IoK8sApimachineryPkgApiResourceQuantity=None, resource: str=None):  # noqa: E501
        """IoK8sApiCoreV1ResourceFieldSelector - a model defined in Swagger

        :param container_name: The container_name of this IoK8sApiCoreV1ResourceFieldSelector.  # noqa: E501
        :type container_name: str
        :param divisor: The divisor of this IoK8sApiCoreV1ResourceFieldSelector.  # noqa: E501
        :type divisor: IoK8sApimachineryPkgApiResourceQuantity
        :param resource: The resource of this IoK8sApiCoreV1ResourceFieldSelector.  # noqa: E501
        :type resource: str
        """
        self.swagger_types = {
            'container_name': str,
            'divisor': IoK8sApimachineryPkgApiResourceQuantity,
            'resource': str
        }

        self.attribute_map = {
            'container_name': 'containerName',
            'divisor': 'divisor',
            'resource': 'resource'
        }

        self._container_name = container_name
        self._divisor = divisor
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1ResourceFieldSelector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.ResourceFieldSelector of this IoK8sApiCoreV1ResourceFieldSelector.  # noqa: E501
        :rtype: IoK8sApiCoreV1ResourceFieldSelector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def container_name(self) -> str:
        """Gets the container_name of this IoK8sApiCoreV1ResourceFieldSelector.

        Container name: required for volumes, optional for env vars  # noqa: E501

        :return: The container_name of this IoK8sApiCoreV1ResourceFieldSelector.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name: str):
        """Sets the container_name of this IoK8sApiCoreV1ResourceFieldSelector.

        Container name: required for volumes, optional for env vars  # noqa: E501

        :param container_name: The container_name of this IoK8sApiCoreV1ResourceFieldSelector.
        :type container_name: str
        """

        self._container_name = container_name

    @property
    def divisor(self) -> IoK8sApimachineryPkgApiResourceQuantity:
        """Gets the divisor of this IoK8sApiCoreV1ResourceFieldSelector.

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :return: The divisor of this IoK8sApiCoreV1ResourceFieldSelector.
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor: IoK8sApimachineryPkgApiResourceQuantity):
        """Sets the divisor of this IoK8sApiCoreV1ResourceFieldSelector.

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :param divisor: The divisor of this IoK8sApiCoreV1ResourceFieldSelector.
        :type divisor: IoK8sApimachineryPkgApiResourceQuantity
        """

        self._divisor = divisor

    @property
    def resource(self) -> str:
        """Gets the resource of this IoK8sApiCoreV1ResourceFieldSelector.

        Required: resource to select  # noqa: E501

        :return: The resource of this IoK8sApiCoreV1ResourceFieldSelector.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str):
        """Sets the resource of this IoK8sApiCoreV1ResourceFieldSelector.

        Required: resource to select  # noqa: E501

        :param resource: The resource of this IoK8sApiCoreV1ResourceFieldSelector.
        :type resource: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource