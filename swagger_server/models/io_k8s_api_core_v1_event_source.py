# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1EventSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, component: str=None, host: str=None):  # noqa: E501
        """IoK8sApiCoreV1EventSource - a model defined in Swagger

        :param component: The component of this IoK8sApiCoreV1EventSource.  # noqa: E501
        :type component: str
        :param host: The host of this IoK8sApiCoreV1EventSource.  # noqa: E501
        :type host: str
        """
        self.swagger_types = {
            'component': str,
            'host': str
        }

        self.attribute_map = {
            'component': 'component',
            'host': 'host'
        }

        self._component = component
        self._host = host

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1EventSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.EventSource of this IoK8sApiCoreV1EventSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1EventSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component(self) -> str:
        """Gets the component of this IoK8sApiCoreV1EventSource.

        Component from which the event is generated.  # noqa: E501

        :return: The component of this IoK8sApiCoreV1EventSource.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component: str):
        """Sets the component of this IoK8sApiCoreV1EventSource.

        Component from which the event is generated.  # noqa: E501

        :param component: The component of this IoK8sApiCoreV1EventSource.
        :type component: str
        """

        self._component = component

    @property
    def host(self) -> str:
        """Gets the host of this IoK8sApiCoreV1EventSource.

        Node name on which the event is generated.  # noqa: E501

        :return: The host of this IoK8sApiCoreV1EventSource.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this IoK8sApiCoreV1EventSource.

        Node name on which the event is generated.  # noqa: E501

        :param host: The host of this IoK8sApiCoreV1EventSource.
        :type host: str
        """

        self._host = host
