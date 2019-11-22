# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1Taint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, effect: str=None, key: str=None, time_added: IoK8sApimachineryPkgApisMetaV1Time=None, value: str=None):  # noqa: E501
        """IoK8sApiCoreV1Taint - a model defined in Swagger

        :param effect: The effect of this IoK8sApiCoreV1Taint.  # noqa: E501
        :type effect: str
        :param key: The key of this IoK8sApiCoreV1Taint.  # noqa: E501
        :type key: str
        :param time_added: The time_added of this IoK8sApiCoreV1Taint.  # noqa: E501
        :type time_added: IoK8sApimachineryPkgApisMetaV1Time
        :param value: The value of this IoK8sApiCoreV1Taint.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'effect': str,
            'key': str,
            'time_added': IoK8sApimachineryPkgApisMetaV1Time,
            'value': str
        }

        self.attribute_map = {
            'effect': 'effect',
            'key': 'key',
            'time_added': 'timeAdded',
            'value': 'value'
        }

        self._effect = effect
        self._key = key
        self._time_added = time_added
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1Taint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.Taint of this IoK8sApiCoreV1Taint.  # noqa: E501
        :rtype: IoK8sApiCoreV1Taint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def effect(self) -> str:
        """Gets the effect of this IoK8sApiCoreV1Taint.

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :return: The effect of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect: str):
        """Sets the effect of this IoK8sApiCoreV1Taint.

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :param effect: The effect of this IoK8sApiCoreV1Taint.
        :type effect: str
        """
        if effect is None:
            raise ValueError("Invalid value for `effect`, must not be `None`")  # noqa: E501

        self._effect = effect

    @property
    def key(self) -> str:
        """Gets the key of this IoK8sApiCoreV1Taint.

        Required. The taint key to be applied to a node.  # noqa: E501

        :return: The key of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this IoK8sApiCoreV1Taint.

        Required. The taint key to be applied to a node.  # noqa: E501

        :param key: The key of this IoK8sApiCoreV1Taint.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def time_added(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the time_added of this IoK8sApiCoreV1Taint.

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :return: The time_added of this IoK8sApiCoreV1Taint.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._time_added

    @time_added.setter
    def time_added(self, time_added: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the time_added of this IoK8sApiCoreV1Taint.

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :param time_added: The time_added of this IoK8sApiCoreV1Taint.
        :type time_added: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._time_added = time_added

    @property
    def value(self) -> str:
        """Gets the value of this IoK8sApiCoreV1Taint.

        Required. The taint value corresponding to the taint key.  # noqa: E501

        :return: The value of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this IoK8sApiCoreV1Taint.

        Required. The taint value corresponding to the taint key.  # noqa: E501

        :param value: The value of this IoK8sApiCoreV1Taint.
        :type value: str
        """

        self._value = value
