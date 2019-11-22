# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1NamespaceStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, conditions: List[IoK8sApiCoreV1NamespaceCondition]=None, phase: str=None):  # noqa: E501
        """IoK8sApiCoreV1NamespaceStatus - a model defined in Swagger

        :param conditions: The conditions of this IoK8sApiCoreV1NamespaceStatus.  # noqa: E501
        :type conditions: List[IoK8sApiCoreV1NamespaceCondition]
        :param phase: The phase of this IoK8sApiCoreV1NamespaceStatus.  # noqa: E501
        :type phase: str
        """
        self.swagger_types = {
            'conditions': List[IoK8sApiCoreV1NamespaceCondition],
            'phase': str
        }

        self.attribute_map = {
            'conditions': 'conditions',
            'phase': 'phase'
        }

        self._conditions = conditions
        self._phase = phase

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1NamespaceStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.NamespaceStatus of this IoK8sApiCoreV1NamespaceStatus.  # noqa: E501
        :rtype: IoK8sApiCoreV1NamespaceStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def conditions(self) -> List[IoK8sApiCoreV1NamespaceCondition]:
        """Gets the conditions of this IoK8sApiCoreV1NamespaceStatus.

        Represents the latest available observations of a namespace's current state.  # noqa: E501

        :return: The conditions of this IoK8sApiCoreV1NamespaceStatus.
        :rtype: List[IoK8sApiCoreV1NamespaceCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List[IoK8sApiCoreV1NamespaceCondition]):
        """Sets the conditions of this IoK8sApiCoreV1NamespaceStatus.

        Represents the latest available observations of a namespace's current state.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiCoreV1NamespaceStatus.
        :type conditions: List[IoK8sApiCoreV1NamespaceCondition]
        """

        self._conditions = conditions

    @property
    def phase(self) -> str:
        """Gets the phase of this IoK8sApiCoreV1NamespaceStatus.

        Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/  # noqa: E501

        :return: The phase of this IoK8sApiCoreV1NamespaceStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase: str):
        """Sets the phase of this IoK8sApiCoreV1NamespaceStatus.

        Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/  # noqa: E501

        :param phase: The phase of this IoK8sApiCoreV1NamespaceStatus.
        :type phase: str
        """

        self._phase = phase
