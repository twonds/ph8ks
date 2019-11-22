# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1beta2DaemonSetUpdateStrategy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, rolling_update: IoK8sApiAppsV1beta2RollingUpdateDaemonSet=None, type: str=None):  # noqa: E501
        """IoK8sApiAppsV1beta2DaemonSetUpdateStrategy - a model defined in Swagger

        :param rolling_update: The rolling_update of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.  # noqa: E501
        :type rolling_update: IoK8sApiAppsV1beta2RollingUpdateDaemonSet
        :param type: The type of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'rolling_update': IoK8sApiAppsV1beta2RollingUpdateDaemonSet,
            'type': str
        }

        self.attribute_map = {
            'rolling_update': 'rollingUpdate',
            'type': 'type'
        }

        self._rolling_update = rolling_update
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1beta2DaemonSetUpdateStrategy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1beta2.DaemonSetUpdateStrategy of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.  # noqa: E501
        :rtype: IoK8sApiAppsV1beta2DaemonSetUpdateStrategy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rolling_update(self) -> IoK8sApiAppsV1beta2RollingUpdateDaemonSet:
        """Gets the rolling_update of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.

        Rolling update config params. Present only if type = \"RollingUpdate\".  # noqa: E501

        :return: The rolling_update of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.
        :rtype: IoK8sApiAppsV1beta2RollingUpdateDaemonSet
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update: IoK8sApiAppsV1beta2RollingUpdateDaemonSet):
        """Sets the rolling_update of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.

        Rolling update config params. Present only if type = \"RollingUpdate\".  # noqa: E501

        :param rolling_update: The rolling_update of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.
        :type rolling_update: IoK8sApiAppsV1beta2RollingUpdateDaemonSet
        """

        self._rolling_update = rolling_update

    @property
    def type(self) -> str:
        """Gets the type of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.

        Type of daemon set update. Can be \"RollingUpdate\" or \"OnDelete\". Default is RollingUpdate.  # noqa: E501

        :return: The type of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.

        Type of daemon set update. Can be \"RollingUpdate\" or \"OnDelete\". Default is RollingUpdate.  # noqa: E501

        :param type: The type of this IoK8sApiAppsV1beta2DaemonSetUpdateStrategy.
        :type type: str
        """

        self._type = type
