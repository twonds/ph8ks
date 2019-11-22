# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1ConfigMapEnvSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, optional: bool=None):  # noqa: E501
        """IoK8sApiCoreV1ConfigMapEnvSource - a model defined in Swagger

        :param name: The name of this IoK8sApiCoreV1ConfigMapEnvSource.  # noqa: E501
        :type name: str
        :param optional: The optional of this IoK8sApiCoreV1ConfigMapEnvSource.  # noqa: E501
        :type optional: bool
        """
        self.swagger_types = {
            'name': str,
            'optional': bool
        }

        self.attribute_map = {
            'name': 'name',
            'optional': 'optional'
        }

        self._name = name
        self._optional = optional

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1ConfigMapEnvSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.ConfigMapEnvSource of this IoK8sApiCoreV1ConfigMapEnvSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1ConfigMapEnvSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApiCoreV1ConfigMapEnvSource.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :return: The name of this IoK8sApiCoreV1ConfigMapEnvSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApiCoreV1ConfigMapEnvSource.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :param name: The name of this IoK8sApiCoreV1ConfigMapEnvSource.
        :type name: str
        """

        self._name = name

    @property
    def optional(self) -> bool:
        """Gets the optional of this IoK8sApiCoreV1ConfigMapEnvSource.

        Specify whether the ConfigMap must be defined  # noqa: E501

        :return: The optional of this IoK8sApiCoreV1ConfigMapEnvSource.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional: bool):
        """Sets the optional of this IoK8sApiCoreV1ConfigMapEnvSource.

        Specify whether the ConfigMap must be defined  # noqa: E501

        :param optional: The optional of this IoK8sApiCoreV1ConfigMapEnvSource.
        :type optional: bool
        """

        self._optional = optional