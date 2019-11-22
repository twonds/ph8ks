# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1NamespaceCondition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, last_transition_time: IoK8sApimachineryPkgApisMetaV1Time=None, message: str=None, reason: str=None, status: str=None, type: str=None):  # noqa: E501
        """IoK8sApiCoreV1NamespaceCondition - a model defined in Swagger

        :param last_transition_time: The last_transition_time of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :type last_transition_time: IoK8sApimachineryPkgApisMetaV1Time
        :param message: The message of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :type message: str
        :param reason: The reason of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :type reason: str
        :param status: The status of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :type status: str
        :param type: The type of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'last_transition_time': IoK8sApimachineryPkgApisMetaV1Time,
            'message': str,
            'reason': str,
            'status': str,
            'type': str
        }

        self.attribute_map = {
            'last_transition_time': 'lastTransitionTime',
            'message': 'message',
            'reason': 'reason',
            'status': 'status',
            'type': 'type'
        }

        self._last_transition_time = last_transition_time
        self._message = message
        self._reason = reason
        self._status = status
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1NamespaceCondition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.NamespaceCondition of this IoK8sApiCoreV1NamespaceCondition.  # noqa: E501
        :rtype: IoK8sApiCoreV1NamespaceCondition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_transition_time(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the last_transition_time of this IoK8sApiCoreV1NamespaceCondition.


        :return: The last_transition_time of this IoK8sApiCoreV1NamespaceCondition.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the last_transition_time of this IoK8sApiCoreV1NamespaceCondition.


        :param last_transition_time: The last_transition_time of this IoK8sApiCoreV1NamespaceCondition.
        :type last_transition_time: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self) -> str:
        """Gets the message of this IoK8sApiCoreV1NamespaceCondition.


        :return: The message of this IoK8sApiCoreV1NamespaceCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this IoK8sApiCoreV1NamespaceCondition.


        :param message: The message of this IoK8sApiCoreV1NamespaceCondition.
        :type message: str
        """

        self._message = message

    @property
    def reason(self) -> str:
        """Gets the reason of this IoK8sApiCoreV1NamespaceCondition.


        :return: The reason of this IoK8sApiCoreV1NamespaceCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this IoK8sApiCoreV1NamespaceCondition.


        :param reason: The reason of this IoK8sApiCoreV1NamespaceCondition.
        :type reason: str
        """

        self._reason = reason

    @property
    def status(self) -> str:
        """Gets the status of this IoK8sApiCoreV1NamespaceCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this IoK8sApiCoreV1NamespaceCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this IoK8sApiCoreV1NamespaceCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this IoK8sApiCoreV1NamespaceCondition.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self) -> str:
        """Gets the type of this IoK8sApiCoreV1NamespaceCondition.

        Type of namespace controller condition.  # noqa: E501

        :return: The type of this IoK8sApiCoreV1NamespaceCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IoK8sApiCoreV1NamespaceCondition.

        Type of namespace controller condition.  # noqa: E501

        :param type: The type of this IoK8sApiCoreV1NamespaceCondition.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
