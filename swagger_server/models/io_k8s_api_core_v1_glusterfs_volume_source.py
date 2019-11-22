# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1GlusterfsVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, endpoints: str=None, path: str=None, read_only: bool=None):  # noqa: E501
        """IoK8sApiCoreV1GlusterfsVolumeSource - a model defined in Swagger

        :param endpoints: The endpoints of this IoK8sApiCoreV1GlusterfsVolumeSource.  # noqa: E501
        :type endpoints: str
        :param path: The path of this IoK8sApiCoreV1GlusterfsVolumeSource.  # noqa: E501
        :type path: str
        :param read_only: The read_only of this IoK8sApiCoreV1GlusterfsVolumeSource.  # noqa: E501
        :type read_only: bool
        """
        self.swagger_types = {
            'endpoints': str,
            'path': str,
            'read_only': bool
        }

        self.attribute_map = {
            'endpoints': 'endpoints',
            'path': 'path',
            'read_only': 'readOnly'
        }

        self._endpoints = endpoints
        self._path = path
        self._read_only = read_only

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1GlusterfsVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.GlusterfsVolumeSource of this IoK8sApiCoreV1GlusterfsVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1GlusterfsVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def endpoints(self) -> str:
        """Gets the endpoints of this IoK8sApiCoreV1GlusterfsVolumeSource.

        EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The endpoints of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: str):
        """Sets the endpoints of this IoK8sApiCoreV1GlusterfsVolumeSource.

        EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param endpoints: The endpoints of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :type endpoints: str
        """
        if endpoints is None:
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def path(self) -> str:
        """Gets the path of this IoK8sApiCoreV1GlusterfsVolumeSource.

        Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The path of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IoK8sApiCoreV1GlusterfsVolumeSource.

        Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param path: The path of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def read_only(self) -> bool:
        """Gets the read_only of this IoK8sApiCoreV1GlusterfsVolumeSource.

        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The read_only of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: bool):
        """Sets the read_only of this IoK8sApiCoreV1GlusterfsVolumeSource.

        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param read_only: The read_only of this IoK8sApiCoreV1GlusterfsVolumeSource.
        :type read_only: bool
        """

        self._read_only = read_only