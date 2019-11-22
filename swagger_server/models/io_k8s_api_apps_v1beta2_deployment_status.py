# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1beta2DeploymentStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, available_replicas: int=None, collision_count: int=None, conditions: List[IoK8sApiAppsV1beta2DeploymentCondition]=None, observed_generation: int=None, ready_replicas: int=None, replicas: int=None, unavailable_replicas: int=None, updated_replicas: int=None):  # noqa: E501
        """IoK8sApiAppsV1beta2DeploymentStatus - a model defined in Swagger

        :param available_replicas: The available_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type available_replicas: int
        :param collision_count: The collision_count of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type collision_count: int
        :param conditions: The conditions of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type conditions: List[IoK8sApiAppsV1beta2DeploymentCondition]
        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type observed_generation: int
        :param ready_replicas: The ready_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type ready_replicas: int
        :param replicas: The replicas of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type replicas: int
        :param unavailable_replicas: The unavailable_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type unavailable_replicas: int
        :param updated_replicas: The updated_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :type updated_replicas: int
        """
        self.swagger_types = {
            'available_replicas': int,
            'collision_count': int,
            'conditions': List[IoK8sApiAppsV1beta2DeploymentCondition],
            'observed_generation': int,
            'ready_replicas': int,
            'replicas': int,
            'unavailable_replicas': int,
            'updated_replicas': int
        }

        self.attribute_map = {
            'available_replicas': 'availableReplicas',
            'collision_count': 'collisionCount',
            'conditions': 'conditions',
            'observed_generation': 'observedGeneration',
            'ready_replicas': 'readyReplicas',
            'replicas': 'replicas',
            'unavailable_replicas': 'unavailableReplicas',
            'updated_replicas': 'updatedReplicas'
        }

        self._available_replicas = available_replicas
        self._collision_count = collision_count
        self._conditions = conditions
        self._observed_generation = observed_generation
        self._ready_replicas = ready_replicas
        self._replicas = replicas
        self._unavailable_replicas = unavailable_replicas
        self._updated_replicas = updated_replicas

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1beta2DeploymentStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1beta2.DeploymentStatus of this IoK8sApiAppsV1beta2DeploymentStatus.  # noqa: E501
        :rtype: IoK8sApiAppsV1beta2DeploymentStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def available_replicas(self) -> int:
        """Gets the available_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.  # noqa: E501

        :return: The available_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas: int):
        """Sets the available_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.  # noqa: E501

        :param available_replicas: The available_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def collision_count(self) -> int:
        """Gets the collision_count of this IoK8sApiAppsV1beta2DeploymentStatus.

        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.  # noqa: E501

        :return: The collision_count of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count: int):
        """Sets the collision_count of this IoK8sApiAppsV1beta2DeploymentStatus.

        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.  # noqa: E501

        :param collision_count: The collision_count of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type collision_count: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self) -> List[IoK8sApiAppsV1beta2DeploymentCondition]:
        """Gets the conditions of this IoK8sApiAppsV1beta2DeploymentStatus.

        Represents the latest available observations of a deployment's current state.  # noqa: E501

        :return: The conditions of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: List[IoK8sApiAppsV1beta2DeploymentCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List[IoK8sApiAppsV1beta2DeploymentCondition]):
        """Sets the conditions of this IoK8sApiAppsV1beta2DeploymentStatus.

        Represents the latest available observations of a deployment's current state.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type conditions: List[IoK8sApiAppsV1beta2DeploymentCondition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self) -> int:
        """Gets the observed_generation of this IoK8sApiAppsV1beta2DeploymentStatus.

        The generation observed by the deployment controller.  # noqa: E501

        :return: The observed_generation of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation: int):
        """Sets the observed_generation of this IoK8sApiAppsV1beta2DeploymentStatus.

        The generation observed by the deployment controller.  # noqa: E501

        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self) -> int:
        """Gets the ready_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of ready pods targeted by this deployment.  # noqa: E501

        :return: The ready_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas: int):
        """Sets the ready_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of ready pods targeted by this deployment.  # noqa: E501

        :param ready_replicas: The ready_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type ready_replicas: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment (their labels match the selector).  # noqa: E501

        :return: The replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment (their labels match the selector).  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type replicas: int
        """

        self._replicas = replicas

    @property
    def unavailable_replicas(self) -> int:
        """Gets the unavailable_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.  # noqa: E501

        :return: The unavailable_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas: int):
        """Sets the unavailable_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.  # noqa: E501

        :param unavailable_replicas: The unavailable_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type unavailable_replicas: int
        """

        self._unavailable_replicas = unavailable_replicas

    @property
    def updated_replicas(self) -> int:
        """Gets the updated_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment that have the desired template spec.  # noqa: E501

        :return: The updated_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas: int):
        """Sets the updated_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment that have the desired template spec.  # noqa: E501

        :param updated_replicas: The updated_replicas of this IoK8sApiAppsV1beta2DeploymentStatus.
        :type updated_replicas: int
        """

        self._updated_replicas = updated_replicas
