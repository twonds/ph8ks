# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthenticationV1beta1UserInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, extra: Dict[str, List[str]]=None, groups: List[str]=None, uid: str=None, username: str=None):  # noqa: E501
        """IoK8sApiAuthenticationV1beta1UserInfo - a model defined in Swagger

        :param extra: The extra of this IoK8sApiAuthenticationV1beta1UserInfo.  # noqa: E501
        :type extra: Dict[str, List[str]]
        :param groups: The groups of this IoK8sApiAuthenticationV1beta1UserInfo.  # noqa: E501
        :type groups: List[str]
        :param uid: The uid of this IoK8sApiAuthenticationV1beta1UserInfo.  # noqa: E501
        :type uid: str
        :param username: The username of this IoK8sApiAuthenticationV1beta1UserInfo.  # noqa: E501
        :type username: str
        """
        self.swagger_types = {
            'extra': Dict[str, List[str]],
            'groups': List[str],
            'uid': str,
            'username': str
        }

        self.attribute_map = {
            'extra': 'extra',
            'groups': 'groups',
            'uid': 'uid',
            'username': 'username'
        }

        self._extra = extra
        self._groups = groups
        self._uid = uid
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthenticationV1beta1UserInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authentication.v1beta1.UserInfo of this IoK8sApiAuthenticationV1beta1UserInfo.  # noqa: E501
        :rtype: IoK8sApiAuthenticationV1beta1UserInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extra(self) -> Dict[str, List[str]]:
        """Gets the extra of this IoK8sApiAuthenticationV1beta1UserInfo.

        Any additional information provided by the authenticator.  # noqa: E501

        :return: The extra of this IoK8sApiAuthenticationV1beta1UserInfo.
        :rtype: Dict[str, List[str]]
        """
        return self._extra

    @extra.setter
    def extra(self, extra: Dict[str, List[str]]):
        """Sets the extra of this IoK8sApiAuthenticationV1beta1UserInfo.

        Any additional information provided by the authenticator.  # noqa: E501

        :param extra: The extra of this IoK8sApiAuthenticationV1beta1UserInfo.
        :type extra: Dict[str, List[str]]
        """

        self._extra = extra

    @property
    def groups(self) -> List[str]:
        """Gets the groups of this IoK8sApiAuthenticationV1beta1UserInfo.

        The names of groups this user is a part of.  # noqa: E501

        :return: The groups of this IoK8sApiAuthenticationV1beta1UserInfo.
        :rtype: List[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: List[str]):
        """Sets the groups of this IoK8sApiAuthenticationV1beta1UserInfo.

        The names of groups this user is a part of.  # noqa: E501

        :param groups: The groups of this IoK8sApiAuthenticationV1beta1UserInfo.
        :type groups: List[str]
        """

        self._groups = groups

    @property
    def uid(self) -> str:
        """Gets the uid of this IoK8sApiAuthenticationV1beta1UserInfo.

        A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.  # noqa: E501

        :return: The uid of this IoK8sApiAuthenticationV1beta1UserInfo.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this IoK8sApiAuthenticationV1beta1UserInfo.

        A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.  # noqa: E501

        :param uid: The uid of this IoK8sApiAuthenticationV1beta1UserInfo.
        :type uid: str
        """

        self._uid = uid

    @property
    def username(self) -> str:
        """Gets the username of this IoK8sApiAuthenticationV1beta1UserInfo.

        The name that uniquely identifies this user among all active users.  # noqa: E501

        :return: The username of this IoK8sApiAuthenticationV1beta1UserInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this IoK8sApiAuthenticationV1beta1UserInfo.

        The name that uniquely identifies this user among all active users.  # noqa: E501

        :param username: The username of this IoK8sApiAuthenticationV1beta1UserInfo.
        :type username: str
        """

        self._username = username
