# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAutoscalingV1ScaleStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, replicas: int=None, selector: str=None):  # noqa: E501
        """IoK8sApiAutoscalingV1ScaleStatus - a model defined in Swagger

        :param replicas: The replicas of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :type replicas: int
        :param selector: The selector of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :type selector: str
        """
        self.swagger_types = {
            'replicas': int,
            'selector': str
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'selector': 'selector'
        }

        self._replicas = replicas
        self._selector = selector

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAutoscalingV1ScaleStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.autoscaling.v1.ScaleStatus of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV1ScaleStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiAutoscalingV1ScaleStatus.

        actual number of observed instances of the scaled object.  # noqa: E501

        :return: The replicas of this IoK8sApiAutoscalingV1ScaleStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiAutoscalingV1ScaleStatus.

        actual number of observed instances of the scaled object.  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAutoscalingV1ScaleStatus.
        :type replicas: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def selector(self) -> str:
        """Gets the selector of this IoK8sApiAutoscalingV1ScaleStatus.

        label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :return: The selector of this IoK8sApiAutoscalingV1ScaleStatus.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector: str):
        """Sets the selector of this IoK8sApiAutoscalingV1ScaleStatus.

        label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :param selector: The selector of this IoK8sApiAutoscalingV1ScaleStatus.
        :type selector: str
        """

        self._selector = selector