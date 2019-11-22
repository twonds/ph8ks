# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1Event(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, api_version: str=None, count: int=None, event_time: IoK8sApimachineryPkgApisMetaV1MicroTime=None, first_timestamp: IoK8sApimachineryPkgApisMetaV1Time=None, involved_object: IoK8sApiCoreV1ObjectReference=None, kind: str=None, last_timestamp: IoK8sApimachineryPkgApisMetaV1Time=None, message: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, reason: str=None, related: IoK8sApiCoreV1ObjectReference=None, reporting_component: str=None, reporting_instance: str=None, series: IoK8sApiCoreV1EventSeries=None, source: IoK8sApiCoreV1EventSource=None, type: str=None):  # noqa: E501
        """IoK8sApiCoreV1Event - a model defined in Swagger

        :param action: The action of this IoK8sApiCoreV1Event.  # noqa: E501
        :type action: str
        :param api_version: The api_version of this IoK8sApiCoreV1Event.  # noqa: E501
        :type api_version: str
        :param count: The count of this IoK8sApiCoreV1Event.  # noqa: E501
        :type count: int
        :param event_time: The event_time of this IoK8sApiCoreV1Event.  # noqa: E501
        :type event_time: IoK8sApimachineryPkgApisMetaV1MicroTime
        :param first_timestamp: The first_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :type first_timestamp: IoK8sApimachineryPkgApisMetaV1Time
        :param involved_object: The involved_object of this IoK8sApiCoreV1Event.  # noqa: E501
        :type involved_object: IoK8sApiCoreV1ObjectReference
        :param kind: The kind of this IoK8sApiCoreV1Event.  # noqa: E501
        :type kind: str
        :param last_timestamp: The last_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :type last_timestamp: IoK8sApimachineryPkgApisMetaV1Time
        :param message: The message of this IoK8sApiCoreV1Event.  # noqa: E501
        :type message: str
        :param metadata: The metadata of this IoK8sApiCoreV1Event.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param reason: The reason of this IoK8sApiCoreV1Event.  # noqa: E501
        :type reason: str
        :param related: The related of this IoK8sApiCoreV1Event.  # noqa: E501
        :type related: IoK8sApiCoreV1ObjectReference
        :param reporting_component: The reporting_component of this IoK8sApiCoreV1Event.  # noqa: E501
        :type reporting_component: str
        :param reporting_instance: The reporting_instance of this IoK8sApiCoreV1Event.  # noqa: E501
        :type reporting_instance: str
        :param series: The series of this IoK8sApiCoreV1Event.  # noqa: E501
        :type series: IoK8sApiCoreV1EventSeries
        :param source: The source of this IoK8sApiCoreV1Event.  # noqa: E501
        :type source: IoK8sApiCoreV1EventSource
        :param type: The type of this IoK8sApiCoreV1Event.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'action': str,
            'api_version': str,
            'count': int,
            'event_time': IoK8sApimachineryPkgApisMetaV1MicroTime,
            'first_timestamp': IoK8sApimachineryPkgApisMetaV1Time,
            'involved_object': IoK8sApiCoreV1ObjectReference,
            'kind': str,
            'last_timestamp': IoK8sApimachineryPkgApisMetaV1Time,
            'message': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'reason': str,
            'related': IoK8sApiCoreV1ObjectReference,
            'reporting_component': str,
            'reporting_instance': str,
            'series': IoK8sApiCoreV1EventSeries,
            'source': IoK8sApiCoreV1EventSource,
            'type': str
        }

        self.attribute_map = {
            'action': 'action',
            'api_version': 'apiVersion',
            'count': 'count',
            'event_time': 'eventTime',
            'first_timestamp': 'firstTimestamp',
            'involved_object': 'involvedObject',
            'kind': 'kind',
            'last_timestamp': 'lastTimestamp',
            'message': 'message',
            'metadata': 'metadata',
            'reason': 'reason',
            'related': 'related',
            'reporting_component': 'reportingComponent',
            'reporting_instance': 'reportingInstance',
            'series': 'series',
            'source': 'source',
            'type': 'type'
        }

        self._action = action
        self._api_version = api_version
        self._count = count
        self._event_time = event_time
        self._first_timestamp = first_timestamp
        self._involved_object = involved_object
        self._kind = kind
        self._last_timestamp = last_timestamp
        self._message = message
        self._metadata = metadata
        self._reason = reason
        self._related = related
        self._reporting_component = reporting_component
        self._reporting_instance = reporting_instance
        self._series = series
        self._source = source
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1Event':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.Event of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApiCoreV1Event
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self) -> str:
        """Gets the action of this IoK8sApiCoreV1Event.

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :return: The action of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this IoK8sApiCoreV1Event.

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :param action: The action of this IoK8sApiCoreV1Event.
        :type action: str
        """

        self._action = action

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiCoreV1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiCoreV1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiCoreV1Event.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def count(self) -> int:
        """Gets the count of this IoK8sApiCoreV1Event.

        The number of times this event has occurred.  # noqa: E501

        :return: The count of this IoK8sApiCoreV1Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this IoK8sApiCoreV1Event.

        The number of times this event has occurred.  # noqa: E501

        :param count: The count of this IoK8sApiCoreV1Event.
        :type count: int
        """

        self._count = count

    @property
    def event_time(self) -> IoK8sApimachineryPkgApisMetaV1MicroTime:
        """Gets the event_time of this IoK8sApiCoreV1Event.

        Time when this Event was first observed.  # noqa: E501

        :return: The event_time of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApimachineryPkgApisMetaV1MicroTime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: IoK8sApimachineryPkgApisMetaV1MicroTime):
        """Sets the event_time of this IoK8sApiCoreV1Event.

        Time when this Event was first observed.  # noqa: E501

        :param event_time: The event_time of this IoK8sApiCoreV1Event.
        :type event_time: IoK8sApimachineryPkgApisMetaV1MicroTime
        """

        self._event_time = event_time

    @property
    def first_timestamp(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the first_timestamp of this IoK8sApiCoreV1Event.

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :return: The first_timestamp of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the first_timestamp of this IoK8sApiCoreV1Event.

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :param first_timestamp: The first_timestamp of this IoK8sApiCoreV1Event.
        :type first_timestamp: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self) -> IoK8sApiCoreV1ObjectReference:
        """Gets the involved_object of this IoK8sApiCoreV1Event.

        The object that this event is about.  # noqa: E501

        :return: The involved_object of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object: IoK8sApiCoreV1ObjectReference):
        """Sets the involved_object of this IoK8sApiCoreV1Event.

        The object that this event is about.  # noqa: E501

        :param involved_object: The involved_object of this IoK8sApiCoreV1Event.
        :type involved_object: IoK8sApiCoreV1ObjectReference
        """
        if involved_object is None:
            raise ValueError("Invalid value for `involved_object`, must not be `None`")  # noqa: E501

        self._involved_object = involved_object

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiCoreV1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiCoreV1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiCoreV1Event.
        :type kind: str
        """

        self._kind = kind

    @property
    def last_timestamp(self) -> IoK8sApimachineryPkgApisMetaV1Time:
        """Gets the last_timestamp of this IoK8sApiCoreV1Event.

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :return: The last_timestamp of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp: IoK8sApimachineryPkgApisMetaV1Time):
        """Sets the last_timestamp of this IoK8sApiCoreV1Event.

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :param last_timestamp: The last_timestamp of this IoK8sApiCoreV1Event.
        :type last_timestamp: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self) -> str:
        """Gets the message of this IoK8sApiCoreV1Event.

        A human-readable description of the status of this operation.  # noqa: E501

        :return: The message of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this IoK8sApiCoreV1Event.

        A human-readable description of the status of this operation.  # noqa: E501

        :param message: The message of this IoK8sApiCoreV1Event.
        :type message: str
        """

        self._message = message

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiCoreV1Event.

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiCoreV1Event.

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiCoreV1Event.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def reason(self) -> str:
        """Gets the reason of this IoK8sApiCoreV1Event.

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :return: The reason of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this IoK8sApiCoreV1Event.

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :param reason: The reason of this IoK8sApiCoreV1Event.
        :type reason: str
        """

        self._reason = reason

    @property
    def related(self) -> IoK8sApiCoreV1ObjectReference:
        """Gets the related of this IoK8sApiCoreV1Event.

        Optional secondary object for more complex actions.  # noqa: E501

        :return: The related of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related: IoK8sApiCoreV1ObjectReference):
        """Sets the related of this IoK8sApiCoreV1Event.

        Optional secondary object for more complex actions.  # noqa: E501

        :param related: The related of this IoK8sApiCoreV1Event.
        :type related: IoK8sApiCoreV1ObjectReference
        """

        self._related = related

    @property
    def reporting_component(self) -> str:
        """Gets the reporting_component of this IoK8sApiCoreV1Event.

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :return: The reporting_component of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component: str):
        """Sets the reporting_component of this IoK8sApiCoreV1Event.

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :param reporting_component: The reporting_component of this IoK8sApiCoreV1Event.
        :type reporting_component: str
        """

        self._reporting_component = reporting_component

    @property
    def reporting_instance(self) -> str:
        """Gets the reporting_instance of this IoK8sApiCoreV1Event.

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :return: The reporting_instance of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance: str):
        """Sets the reporting_instance of this IoK8sApiCoreV1Event.

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :param reporting_instance: The reporting_instance of this IoK8sApiCoreV1Event.
        :type reporting_instance: str
        """

        self._reporting_instance = reporting_instance

    @property
    def series(self) -> IoK8sApiCoreV1EventSeries:
        """Gets the series of this IoK8sApiCoreV1Event.

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :return: The series of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApiCoreV1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series: IoK8sApiCoreV1EventSeries):
        """Sets the series of this IoK8sApiCoreV1Event.

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :param series: The series of this IoK8sApiCoreV1Event.
        :type series: IoK8sApiCoreV1EventSeries
        """

        self._series = series

    @property
    def source(self) -> IoK8sApiCoreV1EventSource:
        """Gets the source of this IoK8sApiCoreV1Event.

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :return: The source of this IoK8sApiCoreV1Event.
        :rtype: IoK8sApiCoreV1EventSource
        """
        return self._source

    @source.setter
    def source(self, source: IoK8sApiCoreV1EventSource):
        """Sets the source of this IoK8sApiCoreV1Event.

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :param source: The source of this IoK8sApiCoreV1Event.
        :type source: IoK8sApiCoreV1EventSource
        """

        self._source = source

    @property
    def type(self) -> str:
        """Gets the type of this IoK8sApiCoreV1Event.

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :return: The type of this IoK8sApiCoreV1Event.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IoK8sApiCoreV1Event.

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :param type: The type of this IoK8sApiCoreV1Event.
        :type type: str
        """

        self._type = type
