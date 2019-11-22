# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1CephFSPersistentVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, monitors: List[str]=None, path: str=None, read_only: bool=None, secret_file: str=None, secret_ref: IoK8sApiCoreV1SecretReference=None, user: str=None):  # noqa: E501
        """IoK8sApiCoreV1CephFSPersistentVolumeSource - a model defined in Swagger

        :param monitors: The monitors of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type monitors: List[str]
        :param path: The path of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type path: str
        :param read_only: The read_only of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type read_only: bool
        :param secret_file: The secret_file of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type secret_file: str
        :param secret_ref: The secret_ref of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type secret_ref: IoK8sApiCoreV1SecretReference
        :param user: The user of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :type user: str
        """
        self.swagger_types = {
            'monitors': List[str],
            'path': str,
            'read_only': bool,
            'secret_file': str,
            'secret_ref': IoK8sApiCoreV1SecretReference,
            'user': str
        }

        self.attribute_map = {
            'monitors': 'monitors',
            'path': 'path',
            'read_only': 'readOnly',
            'secret_file': 'secretFile',
            'secret_ref': 'secretRef',
            'user': 'user'
        }

        self._monitors = monitors
        self._path = path
        self._read_only = read_only
        self._secret_file = secret_file
        self._secret_ref = secret_ref
        self._user = user

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1CephFSPersistentVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.CephFSPersistentVolumeSource of this IoK8sApiCoreV1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1CephFSPersistentVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def monitors(self) -> List[str]:
        """Gets the monitors of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The monitors of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: List[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors: List[str]):
        """Sets the monitors of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param monitors: The monitors of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type monitors: List[str]
        """
        if monitors is None:
            raise ValueError("Invalid value for `monitors`, must not be `None`")  # noqa: E501

        self._monitors = monitors

    @property
    def path(self) -> str:
        """Gets the path of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: Used as the mounted root, rather than the full Ceph tree, default is /  # noqa: E501

        :return: The path of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: Used as the mounted root, rather than the full Ceph tree, default is /  # noqa: E501

        :param path: The path of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type path: str
        """

        self._path = path

    @property
    def read_only(self) -> bool:
        """Gets the read_only of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The read_only of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: bool):
        """Sets the read_only of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param read_only: The read_only of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def secret_file(self) -> str:
        """Gets the secret_file of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The secret_file of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: str
        """
        return self._secret_file

    @secret_file.setter
    def secret_file(self, secret_file: str):
        """Sets the secret_file of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param secret_file: The secret_file of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type secret_file: str
        """

        self._secret_file = secret_file

    @property
    def secret_ref(self) -> IoK8sApiCoreV1SecretReference:
        """Gets the secret_ref of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The secret_ref of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: IoK8sApiCoreV1SecretReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref: IoK8sApiCoreV1SecretReference):
        """Sets the secret_ref of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param secret_ref: The secret_ref of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type secret_ref: IoK8sApiCoreV1SecretReference
        """

        self._secret_ref = secret_ref

    @property
    def user(self) -> str:
        """Gets the user of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The user of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this IoK8sApiCoreV1CephFSPersistentVolumeSource.

        Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param user: The user of this IoK8sApiCoreV1CephFSPersistentVolumeSource.
        :type user: str
        """

        self._user = user