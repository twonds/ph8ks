# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1EnvFromSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, config_map_ref: IoK8sApiCoreV1ConfigMapEnvSource=None, prefix: str=None, secret_ref: IoK8sApiCoreV1SecretEnvSource=None):  # noqa: E501
        """IoK8sApiCoreV1EnvFromSource - a model defined in Swagger

        :param config_map_ref: The config_map_ref of this IoK8sApiCoreV1EnvFromSource.  # noqa: E501
        :type config_map_ref: IoK8sApiCoreV1ConfigMapEnvSource
        :param prefix: The prefix of this IoK8sApiCoreV1EnvFromSource.  # noqa: E501
        :type prefix: str
        :param secret_ref: The secret_ref of this IoK8sApiCoreV1EnvFromSource.  # noqa: E501
        :type secret_ref: IoK8sApiCoreV1SecretEnvSource
        """
        self.swagger_types = {
            'config_map_ref': IoK8sApiCoreV1ConfigMapEnvSource,
            'prefix': str,
            'secret_ref': IoK8sApiCoreV1SecretEnvSource
        }

        self.attribute_map = {
            'config_map_ref': 'configMapRef',
            'prefix': 'prefix',
            'secret_ref': 'secretRef'
        }

        self._config_map_ref = config_map_ref
        self._prefix = prefix
        self._secret_ref = secret_ref

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1EnvFromSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.EnvFromSource of this IoK8sApiCoreV1EnvFromSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1EnvFromSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_map_ref(self) -> IoK8sApiCoreV1ConfigMapEnvSource:
        """Gets the config_map_ref of this IoK8sApiCoreV1EnvFromSource.

        The ConfigMap to select from  # noqa: E501

        :return: The config_map_ref of this IoK8sApiCoreV1EnvFromSource.
        :rtype: IoK8sApiCoreV1ConfigMapEnvSource
        """
        return self._config_map_ref

    @config_map_ref.setter
    def config_map_ref(self, config_map_ref: IoK8sApiCoreV1ConfigMapEnvSource):
        """Sets the config_map_ref of this IoK8sApiCoreV1EnvFromSource.

        The ConfigMap to select from  # noqa: E501

        :param config_map_ref: The config_map_ref of this IoK8sApiCoreV1EnvFromSource.
        :type config_map_ref: IoK8sApiCoreV1ConfigMapEnvSource
        """

        self._config_map_ref = config_map_ref

    @property
    def prefix(self) -> str:
        """Gets the prefix of this IoK8sApiCoreV1EnvFromSource.

        An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.  # noqa: E501

        :return: The prefix of this IoK8sApiCoreV1EnvFromSource.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str):
        """Sets the prefix of this IoK8sApiCoreV1EnvFromSource.

        An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.  # noqa: E501

        :param prefix: The prefix of this IoK8sApiCoreV1EnvFromSource.
        :type prefix: str
        """

        self._prefix = prefix

    @property
    def secret_ref(self) -> IoK8sApiCoreV1SecretEnvSource:
        """Gets the secret_ref of this IoK8sApiCoreV1EnvFromSource.

        The Secret to select from  # noqa: E501

        :return: The secret_ref of this IoK8sApiCoreV1EnvFromSource.
        :rtype: IoK8sApiCoreV1SecretEnvSource
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref: IoK8sApiCoreV1SecretEnvSource):
        """Sets the secret_ref of this IoK8sApiCoreV1EnvFromSource.

        The Secret to select from  # noqa: E501

        :param secret_ref: The secret_ref of this IoK8sApiCoreV1EnvFromSource.
        :type secret_ref: IoK8sApiCoreV1SecretEnvSource
        """

        self._secret_ref = secret_ref
