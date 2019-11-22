# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1AllowedHostPath(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, path_prefix: str=None, read_only: bool=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1AllowedHostPath - a model defined in Swagger

        :param path_prefix: The path_prefix of this IoK8sApiExtensionsV1beta1AllowedHostPath.  # noqa: E501
        :type path_prefix: str
        :param read_only: The read_only of this IoK8sApiExtensionsV1beta1AllowedHostPath.  # noqa: E501
        :type read_only: bool
        """
        self.swagger_types = {
            'path_prefix': str,
            'read_only': bool
        }

        self.attribute_map = {
            'path_prefix': 'pathPrefix',
            'read_only': 'readOnly'
        }

        self._path_prefix = path_prefix
        self._read_only = read_only

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1AllowedHostPath':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.AllowedHostPath of this IoK8sApiExtensionsV1beta1AllowedHostPath.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1AllowedHostPath
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path_prefix(self) -> str:
        """Gets the path_prefix of this IoK8sApiExtensionsV1beta1AllowedHostPath.

        pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.  Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`  # noqa: E501

        :return: The path_prefix of this IoK8sApiExtensionsV1beta1AllowedHostPath.
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix: str):
        """Sets the path_prefix of this IoK8sApiExtensionsV1beta1AllowedHostPath.

        pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.  Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`  # noqa: E501

        :param path_prefix: The path_prefix of this IoK8sApiExtensionsV1beta1AllowedHostPath.
        :type path_prefix: str
        """

        self._path_prefix = path_prefix

    @property
    def read_only(self) -> bool:
        """Gets the read_only of this IoK8sApiExtensionsV1beta1AllowedHostPath.

        when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.  # noqa: E501

        :return: The read_only of this IoK8sApiExtensionsV1beta1AllowedHostPath.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: bool):
        """Sets the read_only of this IoK8sApiExtensionsV1beta1AllowedHostPath.

        when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.  # noqa: E501

        :param read_only: The read_only of this IoK8sApiExtensionsV1beta1AllowedHostPath.
        :type read_only: bool
        """

        self._read_only = read_only
