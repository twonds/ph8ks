# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1PodReadinessGate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, condition_type: str=None):  # noqa: E501
        """IoK8sApiCoreV1PodReadinessGate - a model defined in Swagger

        :param condition_type: The condition_type of this IoK8sApiCoreV1PodReadinessGate.  # noqa: E501
        :type condition_type: str
        """
        self.swagger_types = {
            'condition_type': str
        }

        self.attribute_map = {
            'condition_type': 'conditionType'
        }

        self._condition_type = condition_type

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1PodReadinessGate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.PodReadinessGate of this IoK8sApiCoreV1PodReadinessGate.  # noqa: E501
        :rtype: IoK8sApiCoreV1PodReadinessGate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def condition_type(self) -> str:
        """Gets the condition_type of this IoK8sApiCoreV1PodReadinessGate.

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :return: The condition_type of this IoK8sApiCoreV1PodReadinessGate.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type: str):
        """Sets the condition_type of this IoK8sApiCoreV1PodReadinessGate.

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :param condition_type: The condition_type of this IoK8sApiCoreV1PodReadinessGate.
        :type condition_type: str
        """
        if condition_type is None:
            raise ValueError("Invalid value for `condition_type`, must not be `None`")  # noqa: E501

        self._condition_type = condition_type