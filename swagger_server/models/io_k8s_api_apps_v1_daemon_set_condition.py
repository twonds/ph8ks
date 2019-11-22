# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1DaemonSetCondition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, last_transition_time: IoK8sApimachineryPkgApisMetaV1Time=None, message: str=None, reason: str=None, status: str=None, type: str=None):  # noqa: E501
        """IoK8sApiAppsV1DaemonSetCondition - a model defined in Swagger

        :param last_transition_time: The last_transition_time of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
        :type last_transition_time: IoK8sApimachineryPkgApisMetaV1Time
        :param message: The message of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
        :type message: str
        :param reason: The reason of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
        :type reason: str
        :param status: The status of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
        :type status: str
        :param type: The type of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1DaemonSetCondition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1.DaemonSetCondition of this IoK8sApiAppsV1DaemonSetCondition.  # noqa: E501
        :rtype: IoK8sApiAppsV1DaemonSetCondition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_transition_time(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the last_transition_time of this IoK8sApiAppsV1DaemonSetCondition.

        Last time the condition transitioned from one status to another.  # noqa: E501

        :return: The last_transition_time of this IoK8sApiAppsV1DaemonSetCondition.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the last_transition_time of this IoK8sApiAppsV1DaemonSetCondition.

        Last time the condition transitioned from one status to another.  # noqa: E501

        :param last_transition_time: The last_transition_time of this IoK8sApiAppsV1DaemonSetCondition.
        :type last_transition_time: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self) -> str:
        """Gets the message of this IoK8sApiAppsV1DaemonSetCondition.

        A human readable message indicating details about the transition.  # noqa: E501

        :return: The message of this IoK8sApiAppsV1DaemonSetCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this IoK8sApiAppsV1DaemonSetCondition.

        A human readable message indicating details about the transition.  # noqa: E501

        :param message: The message of this IoK8sApiAppsV1DaemonSetCondition.
        :type message: str
        """

        self._message = message

    @property
    def reason(self) -> str:
        """Gets the reason of this IoK8sApiAppsV1DaemonSetCondition.

        The reason for the condition's last transition.  # noqa: E501

        :return: The reason of this IoK8sApiAppsV1DaemonSetCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this IoK8sApiAppsV1DaemonSetCondition.

        The reason for the condition's last transition.  # noqa: E501

        :param reason: The reason of this IoK8sApiAppsV1DaemonSetCondition.
        :type reason: str
        """

        self._reason = reason

    @property
    def status(self) -> str:
        """Gets the status of this IoK8sApiAppsV1DaemonSetCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this IoK8sApiAppsV1DaemonSetCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this IoK8sApiAppsV1DaemonSetCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this IoK8sApiAppsV1DaemonSetCondition.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self) -> str:
        """Gets the type of this IoK8sApiAppsV1DaemonSetCondition.

        Type of DaemonSet condition.  # noqa: E501

        :return: The type of this IoK8sApiAppsV1DaemonSetCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IoK8sApiAppsV1DaemonSetCondition.

        Type of DaemonSet condition.  # noqa: E501

        :param type: The type of this IoK8sApiAppsV1DaemonSetCondition.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
