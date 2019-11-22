# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1ServiceAccountTokenProjection(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, audience: str=None, expiration_seconds: int=None, path: str=None):  # noqa: E501
        """IoK8sApiCoreV1ServiceAccountTokenProjection - a model defined in Swagger

        :param audience: The audience of this IoK8sApiCoreV1ServiceAccountTokenProjection.  # noqa: E501
        :type audience: str
        :param expiration_seconds: The expiration_seconds of this IoK8sApiCoreV1ServiceAccountTokenProjection.  # noqa: E501
        :type expiration_seconds: int
        :param path: The path of this IoK8sApiCoreV1ServiceAccountTokenProjection.  # noqa: E501
        :type path: str
        """
        self.swagger_types = {
            'audience': str,
            'expiration_seconds': int,
            'path': str
        }

        self.attribute_map = {
            'audience': 'audience',
            'expiration_seconds': 'expirationSeconds',
            'path': 'path'
        }

        self._audience = audience
        self._expiration_seconds = expiration_seconds
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1ServiceAccountTokenProjection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.ServiceAccountTokenProjection of this IoK8sApiCoreV1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: IoK8sApiCoreV1ServiceAccountTokenProjection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def audience(self) -> str:
        """Gets the audience of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.  # noqa: E501

        :return: The audience of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience: str):
        """Sets the audience of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.  # noqa: E501

        :param audience: The audience of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :type audience: str
        """

        self._audience = audience

    @property
    def expiration_seconds(self) -> int:
        """Gets the expiration_seconds of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.  # noqa: E501

        :return: The expiration_seconds of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds: int):
        """Sets the expiration_seconds of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :type expiration_seconds: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def path(self) -> str:
        """Gets the path of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :return: The path of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IoK8sApiCoreV1ServiceAccountTokenProjection.

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :param path: The path of this IoK8sApiCoreV1ServiceAccountTokenProjection.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path
