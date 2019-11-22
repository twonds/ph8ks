# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAutoscalingV2beta2MetricValueStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, average_utilization: int=None, average_value: IoK8sApimachineryPkgApiResourceQuantity=None, value: IoK8sApimachineryPkgApiResourceQuantity=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta2MetricValueStatus - a model defined in Swagger

        :param average_utilization: The average_utilization of this IoK8sApiAutoscalingV2beta2MetricValueStatus.  # noqa: E501
        :type average_utilization: int
        :param average_value: The average_value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.  # noqa: E501
        :type average_value: IoK8sApimachineryPkgApiResourceQuantity
        :param value: The value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.  # noqa: E501
        :type value: IoK8sApimachineryPkgApiResourceQuantity
        """
        self.swagger_types = {
            'average_utilization': int,
            'average_value': IoK8sApimachineryPkgApiResourceQuantity,
            'value': IoK8sApimachineryPkgApiResourceQuantity
        }

        self.attribute_map = {
            'average_utilization': 'averageUtilization',
            'average_value': 'averageValue',
            'value': 'value'
        }

        self._average_utilization = average_utilization
        self._average_value = average_value
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAutoscalingV2beta2MetricValueStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.autoscaling.v2beta2.MetricValueStatus of this IoK8sApiAutoscalingV2beta2MetricValueStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2MetricValueStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_utilization(self) -> int:
        """Gets the average_utilization of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :return: The average_utilization of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :rtype: int
        """
        return self._average_utilization

    @average_utilization.setter
    def average_utilization(self, average_utilization: int):
        """Sets the average_utilization of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :param average_utilization: The average_utilization of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :type average_utilization: int
        """

        self._average_utilization = average_utilization

    @property
    def average_value(self) -> IoK8sApimachineryPkgApiResourceQuantity:
        """Gets the average_value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The average_value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value: IoK8sApimachineryPkgApiResourceQuantity):
        """Sets the average_value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param average_value: The average_value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :type average_value: IoK8sApimachineryPkgApiResourceQuantity
        """

        self._average_value = average_value

    @property
    def value(self) -> IoK8sApimachineryPkgApiResourceQuantity:
        """Gets the value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        value is the current value of the metric (as a quantity).  # noqa: E501

        :return: The value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._value

    @value.setter
    def value(self, value: IoK8sApimachineryPkgApiResourceQuantity):
        """Sets the value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.

        value is the current value of the metric (as a quantity).  # noqa: E501

        :param value: The value of this IoK8sApiAutoscalingV2beta2MetricValueStatus.
        :type value: IoK8sApimachineryPkgApiResourceQuantity
        """

        self._value = value