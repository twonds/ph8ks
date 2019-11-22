# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1beta2ReplicaSetStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, available_replicas: int=None, conditions: List[IoK8sApiAppsV1beta2ReplicaSetCondition]=None, fully_labeled_replicas: int=None, observed_generation: int=None, ready_replicas: int=None, replicas: int=None):  # noqa: E501
        """IoK8sApiAppsV1beta2ReplicaSetStatus - a model defined in Swagger

        :param available_replicas: The available_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type available_replicas: int
        :param conditions: The conditions of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type conditions: List[IoK8sApiAppsV1beta2ReplicaSetCondition]
        :param fully_labeled_replicas: The fully_labeled_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type fully_labeled_replicas: int
        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type observed_generation: int
        :param ready_replicas: The ready_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type ready_replicas: int
        :param replicas: The replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :type replicas: int
        """
        self.swagger_types = {
            'available_replicas': int,
            'conditions': List[IoK8sApiAppsV1beta2ReplicaSetCondition],
            'fully_labeled_replicas': int,
            'observed_generation': int,
            'ready_replicas': int,
            'replicas': int
        }

        self.attribute_map = {
            'available_replicas': 'availableReplicas',
            'conditions': 'conditions',
            'fully_labeled_replicas': 'fullyLabeledReplicas',
            'observed_generation': 'observedGeneration',
            'ready_replicas': 'readyReplicas',
            'replicas': 'replicas'
        }

        self._available_replicas = available_replicas
        self._conditions = conditions
        self._fully_labeled_replicas = fully_labeled_replicas
        self._observed_generation = observed_generation
        self._ready_replicas = ready_replicas
        self._replicas = replicas

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1beta2ReplicaSetStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1beta2.ReplicaSetStatus of this IoK8sApiAppsV1beta2ReplicaSetStatus.  # noqa: E501
        :rtype: IoK8sApiAppsV1beta2ReplicaSetStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def available_replicas(self) -> int:
        """Gets the available_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of available replicas (ready for at least minReadySeconds) for this replica set.  # noqa: E501

        :return: The available_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas: int):
        """Sets the available_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of available replicas (ready for at least minReadySeconds) for this replica set.  # noqa: E501

        :param available_replicas: The available_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def conditions(self) -> List[IoK8sApiAppsV1beta2ReplicaSetCondition]:
        """Gets the conditions of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        Represents the latest available observations of a replica set's current state.  # noqa: E501

        :return: The conditions of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: List[IoK8sApiAppsV1beta2ReplicaSetCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List[IoK8sApiAppsV1beta2ReplicaSetCondition]):
        """Sets the conditions of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        Represents the latest available observations of a replica set's current state.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type conditions: List[IoK8sApiAppsV1beta2ReplicaSetCondition]
        """

        self._conditions = conditions

    @property
    def fully_labeled_replicas(self) -> int:
        """Gets the fully_labeled_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of pods that have labels matching the labels of the pod template of the replicaset.  # noqa: E501

        :return: The fully_labeled_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: int
        """
        return self._fully_labeled_replicas

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas: int):
        """Sets the fully_labeled_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of pods that have labels matching the labels of the pod template of the replicaset.  # noqa: E501

        :param fully_labeled_replicas: The fully_labeled_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type fully_labeled_replicas: int
        """

        self._fully_labeled_replicas = fully_labeled_replicas

    @property
    def observed_generation(self) -> int:
        """Gets the observed_generation of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.  # noqa: E501

        :return: The observed_generation of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation: int):
        """Sets the observed_generation of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.  # noqa: E501

        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self) -> int:
        """Gets the ready_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of ready replicas for this replica set.  # noqa: E501

        :return: The ready_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas: int):
        """Sets the ready_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        The number of ready replicas for this replica set.  # noqa: E501

        :param ready_replicas: The ready_replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type ready_replicas: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :return: The replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAppsV1beta2ReplicaSetStatus.
        :type replicas: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas
