# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1KeyToPath(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, mode: int=None, path: str=None):  # noqa: E501
        """IoK8sApiCoreV1KeyToPath - a model defined in Swagger

        :param key: The key of this IoK8sApiCoreV1KeyToPath.  # noqa: E501
        :type key: str
        :param mode: The mode of this IoK8sApiCoreV1KeyToPath.  # noqa: E501
        :type mode: int
        :param path: The path of this IoK8sApiCoreV1KeyToPath.  # noqa: E501
        :type path: str
        """
        self.swagger_types = {
            'key': str,
            'mode': int,
            'path': str
        }

        self.attribute_map = {
            'key': 'key',
            'mode': 'mode',
            'path': 'path'
        }

        self._key = key
        self._mode = mode
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1KeyToPath':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.KeyToPath of this IoK8sApiCoreV1KeyToPath.  # noqa: E501
        :rtype: IoK8sApiCoreV1KeyToPath
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """Gets the key of this IoK8sApiCoreV1KeyToPath.

        The key to project.  # noqa: E501

        :return: The key of this IoK8sApiCoreV1KeyToPath.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this IoK8sApiCoreV1KeyToPath.

        The key to project.  # noqa: E501

        :param key: The key of this IoK8sApiCoreV1KeyToPath.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def mode(self) -> int:
        """Gets the mode of this IoK8sApiCoreV1KeyToPath.

        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :return: The mode of this IoK8sApiCoreV1KeyToPath.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode: int):
        """Sets the mode of this IoK8sApiCoreV1KeyToPath.

        Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :param mode: The mode of this IoK8sApiCoreV1KeyToPath.
        :type mode: int
        """

        self._mode = mode

    @property
    def path(self) -> str:
        """Gets the path of this IoK8sApiCoreV1KeyToPath.

        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.  # noqa: E501

        :return: The path of this IoK8sApiCoreV1KeyToPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IoK8sApiCoreV1KeyToPath.

        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.  # noqa: E501

        :param path: The path of this IoK8sApiCoreV1KeyToPath.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path
