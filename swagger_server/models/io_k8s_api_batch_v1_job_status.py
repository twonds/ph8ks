# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiBatchV1JobStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, active: int=None, completion_time: IoK8sApimachineryPkgApisMetaV1Time=None, conditions: List[IoK8sApiBatchV1JobCondition]=None, failed: int=None, start_time: IoK8sApimachineryPkgApisMetaV1Time=None, succeeded: int=None):  # noqa: E501
        """IoK8sApiBatchV1JobStatus - a model defined in Swagger

        :param active: The active of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type active: int
        :param completion_time: The completion_time of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type completion_time: IoK8sApimachineryPkgApisMetaV1Time
        :param conditions: The conditions of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type conditions: List[IoK8sApiBatchV1JobCondition]
        :param failed: The failed of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type failed: int
        :param start_time: The start_time of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type start_time: IoK8sApimachineryPkgApisMetaV1Time
        :param succeeded: The succeeded of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :type succeeded: int
        """
        self.swagger_types = {
            'active': int,
            'completion_time': IoK8sApimachineryPkgApisMetaV1Time,
            'conditions': List[IoK8sApiBatchV1JobCondition],
            'failed': int,
            'start_time': IoK8sApimachineryPkgApisMetaV1Time,
            'succeeded': int
        }

        self.attribute_map = {
            'active': 'active',
            'completion_time': 'completionTime',
            'conditions': 'conditions',
            'failed': 'failed',
            'start_time': 'startTime',
            'succeeded': 'succeeded'
        }

        self._active = active
        self._completion_time = completion_time
        self._conditions = conditions
        self._failed = failed
        self._start_time = start_time
        self._succeeded = succeeded

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiBatchV1JobStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.batch.v1.JobStatus of this IoK8sApiBatchV1JobStatus.  # noqa: E501
        :rtype: IoK8sApiBatchV1JobStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self) -> int:
        """Gets the active of this IoK8sApiBatchV1JobStatus.

        The number of actively running pods.  # noqa: E501

        :return: The active of this IoK8sApiBatchV1JobStatus.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active: int):
        """Sets the active of this IoK8sApiBatchV1JobStatus.

        The number of actively running pods.  # noqa: E501

        :param active: The active of this IoK8sApiBatchV1JobStatus.
        :type active: int
        """

        self._active = active

    @property
    def completion_time(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the completion_time of this IoK8sApiBatchV1JobStatus.

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The completion_time of this IoK8sApiBatchV1JobStatus.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the completion_time of this IoK8sApiBatchV1JobStatus.

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param completion_time: The completion_time of this IoK8sApiBatchV1JobStatus.
        :type completion_time: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._completion_time = completion_time

    @property
    def conditions(self) -> List[IoK8sApiBatchV1JobCondition]:
        """Gets the conditions of this IoK8sApiBatchV1JobStatus.

        The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The conditions of this IoK8sApiBatchV1JobStatus.
        :rtype: List[IoK8sApiBatchV1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List[IoK8sApiBatchV1JobCondition]):
        """Sets the conditions of this IoK8sApiBatchV1JobStatus.

        The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param conditions: The conditions of this IoK8sApiBatchV1JobStatus.
        :type conditions: List[IoK8sApiBatchV1JobCondition]
        """

        self._conditions = conditions

    @property
    def failed(self) -> int:
        """Gets the failed of this IoK8sApiBatchV1JobStatus.

        The number of pods which reached phase Failed.  # noqa: E501

        :return: The failed of this IoK8sApiBatchV1JobStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed: int):
        """Sets the failed of this IoK8sApiBatchV1JobStatus.

        The number of pods which reached phase Failed.  # noqa: E501

        :param failed: The failed of this IoK8sApiBatchV1JobStatus.
        :type failed: int
        """

        self._failed = failed

    @property
    def start_time(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the start_time of this IoK8sApiBatchV1JobStatus.

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The start_time of this IoK8sApiBatchV1JobStatus.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the start_time of this IoK8sApiBatchV1JobStatus.

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param start_time: The start_time of this IoK8sApiBatchV1JobStatus.
        :type start_time: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._start_time = start_time

    @property
    def succeeded(self) -> int:
        """Gets the succeeded of this IoK8sApiBatchV1JobStatus.

        The number of pods which reached phase Succeeded.  # noqa: E501

        :return: The succeeded of this IoK8sApiBatchV1JobStatus.
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded: int):
        """Sets the succeeded of this IoK8sApiBatchV1JobStatus.

        The number of pods which reached phase Succeeded.  # noqa: E501

        :param succeeded: The succeeded of this IoK8sApiBatchV1JobStatus.
        :type succeeded: int
        """

        self._succeeded = succeeded