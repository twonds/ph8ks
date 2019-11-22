# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1EventSeries(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, last_observed_time: IoK8sApimachineryPkgApisMetaV1MicroTime=None, state: str=None):  # noqa: E501
        """IoK8sApiCoreV1EventSeries - a model defined in Swagger

        :param count: The count of this IoK8sApiCoreV1EventSeries.  # noqa: E501
        :type count: int
        :param last_observed_time: The last_observed_time of this IoK8sApiCoreV1EventSeries.  # noqa: E501
        :type last_observed_time: IoK8sApimachineryPkgApisMetaV1MicroTime
        :param state: The state of this IoK8sApiCoreV1EventSeries.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'count': int,
            'last_observed_time': IoK8sApimachineryPkgApisMetaV1MicroTime,
            'state': str
        }

        self.attribute_map = {
            'count': 'count',
            'last_observed_time': 'lastObservedTime',
            'state': 'state'
        }

        self._count = count
        self._last_observed_time = last_observed_time
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1EventSeries':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.EventSeries of this IoK8sApiCoreV1EventSeries.  # noqa: E501
        :rtype: IoK8sApiCoreV1EventSeries
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this IoK8sApiCoreV1EventSeries.

        Number of occurrences in this series up to the last heartbeat time  # noqa: E501

        :return: The count of this IoK8sApiCoreV1EventSeries.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this IoK8sApiCoreV1EventSeries.

        Number of occurrences in this series up to the last heartbeat time  # noqa: E501

        :param count: The count of this IoK8sApiCoreV1EventSeries.
        :type count: int
        """

        self._count = count

    @property
    def last_observed_time(self) -> IoK8sApimachineryPkgApisMetaV1MicroTime:
        """Gets the last_observed_time of this IoK8sApiCoreV1EventSeries.

        Time of the last occurrence observed  # noqa: E501

        :return: The last_observed_time of this IoK8sApiCoreV1EventSeries.
        :rtype: IoK8sApimachineryPkgApisMetaV1MicroTime
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time: IoK8sApimachineryPkgApisMetaV1MicroTime):
        """Sets the last_observed_time of this IoK8sApiCoreV1EventSeries.

        Time of the last occurrence observed  # noqa: E501

        :param last_observed_time: The last_observed_time of this IoK8sApiCoreV1EventSeries.
        :type last_observed_time: IoK8sApimachineryPkgApisMetaV1MicroTime
        """

        self._last_observed_time = last_observed_time

    @property
    def state(self) -> str:
        """Gets the state of this IoK8sApiCoreV1EventSeries.

        State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18  # noqa: E501

        :return: The state of this IoK8sApiCoreV1EventSeries.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this IoK8sApiCoreV1EventSeries.

        State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18  # noqa: E501

        :param state: The state of this IoK8sApiCoreV1EventSeries.
        :type state: str
        """

        self._state = state