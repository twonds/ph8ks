# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1CSIPersistentVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, controller_expand_secret_ref: IoK8sApiCoreV1SecretReference=None, controller_publish_secret_ref: IoK8sApiCoreV1SecretReference=None, driver: str=None, fs_type: str=None, node_publish_secret_ref: IoK8sApiCoreV1SecretReference=None, node_stage_secret_ref: IoK8sApiCoreV1SecretReference=None, read_only: bool=None, volume_attributes: Dict[str, str]=None, volume_handle: str=None):  # noqa: E501
        """IoK8sApiCoreV1CSIPersistentVolumeSource - a model defined in Swagger

        :param controller_expand_secret_ref: The controller_expand_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type controller_expand_secret_ref: IoK8sApiCoreV1SecretReference
        :param controller_publish_secret_ref: The controller_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type controller_publish_secret_ref: IoK8sApiCoreV1SecretReference
        :param driver: The driver of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type driver: str
        :param fs_type: The fs_type of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type fs_type: str
        :param node_publish_secret_ref: The node_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type node_publish_secret_ref: IoK8sApiCoreV1SecretReference
        :param node_stage_secret_ref: The node_stage_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type node_stage_secret_ref: IoK8sApiCoreV1SecretReference
        :param read_only: The read_only of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type read_only: bool
        :param volume_attributes: The volume_attributes of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type volume_attributes: Dict[str, str]
        :param volume_handle: The volume_handle of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :type volume_handle: str
        """
        self.swagger_types = {
            'controller_expand_secret_ref': IoK8sApiCoreV1SecretReference,
            'controller_publish_secret_ref': IoK8sApiCoreV1SecretReference,
            'driver': str,
            'fs_type': str,
            'node_publish_secret_ref': IoK8sApiCoreV1SecretReference,
            'node_stage_secret_ref': IoK8sApiCoreV1SecretReference,
            'read_only': bool,
            'volume_attributes': Dict[str, str],
            'volume_handle': str
        }

        self.attribute_map = {
            'controller_expand_secret_ref': 'controllerExpandSecretRef',
            'controller_publish_secret_ref': 'controllerPublishSecretRef',
            'driver': 'driver',
            'fs_type': 'fsType',
            'node_publish_secret_ref': 'nodePublishSecretRef',
            'node_stage_secret_ref': 'nodeStageSecretRef',
            'read_only': 'readOnly',
            'volume_attributes': 'volumeAttributes',
            'volume_handle': 'volumeHandle'
        }

        self._controller_expand_secret_ref = controller_expand_secret_ref
        self._controller_publish_secret_ref = controller_publish_secret_ref
        self._driver = driver
        self._fs_type = fs_type
        self._node_publish_secret_ref = node_publish_secret_ref
        self._node_stage_secret_ref = node_stage_secret_ref
        self._read_only = read_only
        self._volume_attributes = volume_attributes
        self._volume_handle = volume_handle

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1CSIPersistentVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.CSIPersistentVolumeSource of this IoK8sApiCoreV1CSIPersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1CSIPersistentVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def controller_expand_secret_ref(self) -> IoK8sApiCoreV1SecretReference:
        """Gets the controller_expand_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :return: The controller_expand_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: IoK8sApiCoreV1SecretReference
        """
        return self._controller_expand_secret_ref

    @controller_expand_secret_ref.setter
    def controller_expand_secret_ref(self, controller_expand_secret_ref: IoK8sApiCoreV1SecretReference):
        """Sets the controller_expand_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :param controller_expand_secret_ref: The controller_expand_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type controller_expand_secret_ref: IoK8sApiCoreV1SecretReference
        """

        self._controller_expand_secret_ref = controller_expand_secret_ref

    @property
    def controller_publish_secret_ref(self) -> IoK8sApiCoreV1SecretReference:
        """Gets the controller_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :return: The controller_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: IoK8sApiCoreV1SecretReference
        """
        return self._controller_publish_secret_ref

    @controller_publish_secret_ref.setter
    def controller_publish_secret_ref(self, controller_publish_secret_ref: IoK8sApiCoreV1SecretReference):
        """Sets the controller_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :param controller_publish_secret_ref: The controller_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type controller_publish_secret_ref: IoK8sApiCoreV1SecretReference
        """

        self._controller_publish_secret_ref = controller_publish_secret_ref

    @property
    def driver(self) -> str:
        """Gets the driver of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Driver is the name of the driver to use for this volume. Required.  # noqa: E501

        :return: The driver of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver: str):
        """Sets the driver of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Driver is the name of the driver to use for this volume. Required.  # noqa: E501

        :param driver: The driver of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type driver: str
        """
        if driver is None:
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def fs_type(self) -> str:
        """Gets the fs_type of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".  # noqa: E501

        :return: The fs_type of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type: str):
        """Sets the fs_type of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".  # noqa: E501

        :param fs_type: The fs_type of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type fs_type: str
        """

        self._fs_type = fs_type

    @property
    def node_publish_secret_ref(self) -> IoK8sApiCoreV1SecretReference:
        """Gets the node_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :return: The node_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: IoK8sApiCoreV1SecretReference
        """
        return self._node_publish_secret_ref

    @node_publish_secret_ref.setter
    def node_publish_secret_ref(self, node_publish_secret_ref: IoK8sApiCoreV1SecretReference):
        """Sets the node_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :param node_publish_secret_ref: The node_publish_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type node_publish_secret_ref: IoK8sApiCoreV1SecretReference
        """

        self._node_publish_secret_ref = node_publish_secret_ref

    @property
    def node_stage_secret_ref(self) -> IoK8sApiCoreV1SecretReference:
        """Gets the node_stage_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :return: The node_stage_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: IoK8sApiCoreV1SecretReference
        """
        return self._node_stage_secret_ref

    @node_stage_secret_ref.setter
    def node_stage_secret_ref(self, node_stage_secret_ref: IoK8sApiCoreV1SecretReference):
        """Sets the node_stage_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.  # noqa: E501

        :param node_stage_secret_ref: The node_stage_secret_ref of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type node_stage_secret_ref: IoK8sApiCoreV1SecretReference
        """

        self._node_stage_secret_ref = node_stage_secret_ref

    @property
    def read_only(self) -> bool:
        """Gets the read_only of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).  # noqa: E501

        :return: The read_only of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: bool):
        """Sets the read_only of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).  # noqa: E501

        :param read_only: The read_only of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def volume_attributes(self) -> Dict[str, str]:
        """Gets the volume_attributes of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Attributes of the volume to publish.  # noqa: E501

        :return: The volume_attributes of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: Dict[str, str]
        """
        return self._volume_attributes

    @volume_attributes.setter
    def volume_attributes(self, volume_attributes: Dict[str, str]):
        """Sets the volume_attributes of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        Attributes of the volume to publish.  # noqa: E501

        :param volume_attributes: The volume_attributes of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type volume_attributes: Dict[str, str]
        """

        self._volume_attributes = volume_attributes

    @property
    def volume_handle(self) -> str:
        """Gets the volume_handle of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.  # noqa: E501

        :return: The volume_handle of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :rtype: str
        """
        return self._volume_handle

    @volume_handle.setter
    def volume_handle(self, volume_handle: str):
        """Sets the volume_handle of this IoK8sApiCoreV1CSIPersistentVolumeSource.

        VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.  # noqa: E501

        :param volume_handle: The volume_handle of this IoK8sApiCoreV1CSIPersistentVolumeSource.
        :type volume_handle: str
        """
        if volume_handle is None:
            raise ValueError("Invalid value for `volume_handle`, must not be `None`")  # noqa: E501

        self._volume_handle = volume_handle
