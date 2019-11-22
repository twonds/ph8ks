# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1beta2DaemonSetStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, collision_count: int=None, conditions: List[IoK8sApiAppsV1beta2DaemonSetCondition]=None, current_number_scheduled: int=None, desired_number_scheduled: int=None, number_available: int=None, number_misscheduled: int=None, number_ready: int=None, number_unavailable: int=None, observed_generation: int=None, updated_number_scheduled: int=None):  # noqa: E501
        """IoK8sApiAppsV1beta2DaemonSetStatus - a model defined in Swagger

        :param collision_count: The collision_count of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type collision_count: int
        :param conditions: The conditions of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type conditions: List[IoK8sApiAppsV1beta2DaemonSetCondition]
        :param current_number_scheduled: The current_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type current_number_scheduled: int
        :param desired_number_scheduled: The desired_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type desired_number_scheduled: int
        :param number_available: The number_available of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type number_available: int
        :param number_misscheduled: The number_misscheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type number_misscheduled: int
        :param number_ready: The number_ready of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type number_ready: int
        :param number_unavailable: The number_unavailable of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type number_unavailable: int
        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type observed_generation: int
        :param updated_number_scheduled: The updated_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :type updated_number_scheduled: int
        """
        self.swagger_types = {
            'collision_count': int,
            'conditions': List[IoK8sApiAppsV1beta2DaemonSetCondition],
            'current_number_scheduled': int,
            'desired_number_scheduled': int,
            'number_available': int,
            'number_misscheduled': int,
            'number_ready': int,
            'number_unavailable': int,
            'observed_generation': int,
            'updated_number_scheduled': int
        }

        self.attribute_map = {
            'collision_count': 'collisionCount',
            'conditions': 'conditions',
            'current_number_scheduled': 'currentNumberScheduled',
            'desired_number_scheduled': 'desiredNumberScheduled',
            'number_available': 'numberAvailable',
            'number_misscheduled': 'numberMisscheduled',
            'number_ready': 'numberReady',
            'number_unavailable': 'numberUnavailable',
            'observed_generation': 'observedGeneration',
            'updated_number_scheduled': 'updatedNumberScheduled'
        }

        self._collision_count = collision_count
        self._conditions = conditions
        self._current_number_scheduled = current_number_scheduled
        self._desired_number_scheduled = desired_number_scheduled
        self._number_available = number_available
        self._number_misscheduled = number_misscheduled
        self._number_ready = number_ready
        self._number_unavailable = number_unavailable
        self._observed_generation = observed_generation
        self._updated_number_scheduled = updated_number_scheduled

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1beta2DaemonSetStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1beta2.DaemonSetStatus of this IoK8sApiAppsV1beta2DaemonSetStatus.  # noqa: E501
        :rtype: IoK8sApiAppsV1beta2DaemonSetStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def collision_count(self) -> int:
        """Gets the collision_count of this IoK8sApiAppsV1beta2DaemonSetStatus.

        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :return: The collision_count of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count: int):
        """Sets the collision_count of this IoK8sApiAppsV1beta2DaemonSetStatus.

        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :param collision_count: The collision_count of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type collision_count: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self) -> List[IoK8sApiAppsV1beta2DaemonSetCondition]:
        """Gets the conditions of this IoK8sApiAppsV1beta2DaemonSetStatus.

        Represents the latest available observations of a DaemonSet's current state.  # noqa: E501

        :return: The conditions of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: List[IoK8sApiAppsV1beta2DaemonSetCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List[IoK8sApiAppsV1beta2DaemonSetCondition]):
        """Sets the conditions of this IoK8sApiAppsV1beta2DaemonSetStatus.

        Represents the latest available observations of a DaemonSet's current state.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type conditions: List[IoK8sApiAppsV1beta2DaemonSetCondition]
        """

        self._conditions = conditions

    @property
    def current_number_scheduled(self) -> int:
        """Gets the current_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The current_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._current_number_scheduled

    @current_number_scheduled.setter
    def current_number_scheduled(self, current_number_scheduled: int):
        """Sets the current_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param current_number_scheduled: The current_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type current_number_scheduled: int
        """
        if current_number_scheduled is None:
            raise ValueError("Invalid value for `current_number_scheduled`, must not be `None`")  # noqa: E501

        self._current_number_scheduled = current_number_scheduled

    @property
    def desired_number_scheduled(self) -> int:
        """Gets the desired_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The desired_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._desired_number_scheduled

    @desired_number_scheduled.setter
    def desired_number_scheduled(self, desired_number_scheduled: int):
        """Sets the desired_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param desired_number_scheduled: The desired_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type desired_number_scheduled: int
        """
        if desired_number_scheduled is None:
            raise ValueError("Invalid value for `desired_number_scheduled`, must not be `None`")  # noqa: E501

        self._desired_number_scheduled = desired_number_scheduled

    @property
    def number_available(self) -> int:
        """Gets the number_available of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The number_available of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._number_available

    @number_available.setter
    def number_available(self, number_available: int):
        """Sets the number_available of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param number_available: The number_available of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type number_available: int
        """

        self._number_available = number_available

    @property
    def number_misscheduled(self) -> int:
        """Gets the number_misscheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The number_misscheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._number_misscheduled

    @number_misscheduled.setter
    def number_misscheduled(self, number_misscheduled: int):
        """Sets the number_misscheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param number_misscheduled: The number_misscheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type number_misscheduled: int
        """
        if number_misscheduled is None:
            raise ValueError("Invalid value for `number_misscheduled`, must not be `None`")  # noqa: E501

        self._number_misscheduled = number_misscheduled

    @property
    def number_ready(self) -> int:
        """Gets the number_ready of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.  # noqa: E501

        :return: The number_ready of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._number_ready

    @number_ready.setter
    def number_ready(self, number_ready: int):
        """Sets the number_ready of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.  # noqa: E501

        :param number_ready: The number_ready of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type number_ready: int
        """
        if number_ready is None:
            raise ValueError("Invalid value for `number_ready`, must not be `None`")  # noqa: E501

        self._number_ready = number_ready

    @property
    def number_unavailable(self) -> int:
        """Gets the number_unavailable of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The number_unavailable of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._number_unavailable

    @number_unavailable.setter
    def number_unavailable(self, number_unavailable: int):
        """Sets the number_unavailable of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param number_unavailable: The number_unavailable of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type number_unavailable: int
        """

        self._number_unavailable = number_unavailable

    @property
    def observed_generation(self) -> int:
        """Gets the observed_generation of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The most recent generation observed by the daemon set controller.  # noqa: E501

        :return: The observed_generation of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation: int):
        """Sets the observed_generation of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The most recent generation observed by the daemon set controller.  # noqa: E501

        :param observed_generation: The observed_generation of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type observed_generation: int
        """

        self._observed_generation = observed_generation

    @property
    def updated_number_scheduled(self) -> int:
        """Gets the updated_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The total number of nodes that are running updated daemon pod  # noqa: E501

        :return: The updated_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :rtype: int
        """
        return self._updated_number_scheduled

    @updated_number_scheduled.setter
    def updated_number_scheduled(self, updated_number_scheduled: int):
        """Sets the updated_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.

        The total number of nodes that are running updated daemon pod  # noqa: E501

        :param updated_number_scheduled: The updated_number_scheduled of this IoK8sApiAppsV1beta2DaemonSetStatus.
        :type updated_number_scheduled: int
        """

        self._updated_number_scheduled = updated_number_scheduled
