# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1AzureFilePersistentVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, read_only: bool=None, secret_name: str=None, secret_namespace: str=None, share_name: str=None):  # noqa: E501
        """IoK8sApiCoreV1AzureFilePersistentVolumeSource - a model defined in Swagger

        :param read_only: The read_only of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.  # noqa: E501
        :type read_only: bool
        :param secret_name: The secret_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.  # noqa: E501
        :type secret_name: str
        :param secret_namespace: The secret_namespace of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.  # noqa: E501
        :type secret_namespace: str
        :param share_name: The share_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.  # noqa: E501
        :type share_name: str
        """
        self.swagger_types = {
            'read_only': bool,
            'secret_name': str,
            'secret_namespace': str,
            'share_name': str
        }

        self.attribute_map = {
            'read_only': 'readOnly',
            'secret_name': 'secretName',
            'secret_namespace': 'secretNamespace',
            'share_name': 'shareName'
        }

        self._read_only = read_only
        self._secret_name = secret_name
        self._secret_namespace = secret_namespace
        self._share_name = share_name

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1AzureFilePersistentVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.AzureFilePersistentVolumeSource of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1AzureFilePersistentVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def read_only(self) -> bool:
        """Gets the read_only of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :return: The read_only of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: bool):
        """Sets the read_only of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :param read_only: The read_only of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def secret_name(self) -> str:
        """Gets the secret_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        the name of secret that contains Azure Storage Account Name and Key  # noqa: E501

        :return: The secret_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name: str):
        """Sets the secret_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        the name of secret that contains Azure Storage Account Name and Key  # noqa: E501

        :param secret_name: The secret_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :type secret_name: str
        """
        if secret_name is None:
            raise ValueError("Invalid value for `secret_name`, must not be `None`")  # noqa: E501

        self._secret_name = secret_name

    @property
    def secret_namespace(self) -> str:
        """Gets the secret_namespace of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod  # noqa: E501

        :return: The secret_namespace of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._secret_namespace

    @secret_namespace.setter
    def secret_namespace(self, secret_namespace: str):
        """Sets the secret_namespace of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod  # noqa: E501

        :param secret_namespace: The secret_namespace of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :type secret_namespace: str
        """

        self._secret_namespace = secret_namespace

    @property
    def share_name(self) -> str:
        """Gets the share_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        Share Name  # noqa: E501

        :return: The share_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name: str):
        """Sets the share_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.

        Share Name  # noqa: E501

        :param share_name: The share_name of this IoK8sApiCoreV1AzureFilePersistentVolumeSource.
        :type share_name: str
        """
        if share_name is None:
            raise ValueError("Invalid value for `share_name`, must not be `None`")  # noqa: E501

        self._share_name = share_name
