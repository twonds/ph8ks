# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1PhotonPersistentDiskVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, fs_type: str=None, pd_id: str=None):  # noqa: E501
        """IoK8sApiCoreV1PhotonPersistentDiskVolumeSource - a model defined in Swagger

        :param fs_type: The fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type fs_type: str
        :param pd_id: The pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type pd_id: str
        """
        self.swagger_types = {
            'fs_type': str,
            'pd_id': str
        }

        self.attribute_map = {
            'fs_type': 'fsType',
            'pd_id': 'pdID'
        }

        self._fs_type = fs_type
        self._pd_id = pd_id

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1PhotonPersistentDiskVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1PhotonPersistentDiskVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fs_type(self) -> str:
        """Gets the fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type: str):
        """Sets the fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def pd_id(self) -> str:
        """Gets the pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        ID that identifies Photon Controller persistent disk  # noqa: E501

        :return: The pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._pd_id

    @pd_id.setter
    def pd_id(self, pd_id: str):
        """Sets the pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        ID that identifies Photon Controller persistent disk  # noqa: E501

        :param pd_id: The pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.
        :type pd_id: str
        """
        if pd_id is None:
            raise ValueError("Invalid value for `pd_id`, must not be `None`")  # noqa: E501

        self._pd_id = pd_id
