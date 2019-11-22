# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAutoscalingV1CrossVersionObjectReference(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, kind: str=None, name: str=None):  # noqa: E501
        """IoK8sApiAutoscalingV1CrossVersionObjectReference - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiAutoscalingV1CrossVersionObjectReference.  # noqa: E501
        :type api_version: str
        :param kind: The kind of this IoK8sApiAutoscalingV1CrossVersionObjectReference.  # noqa: E501
        :type kind: str
        :param name: The name of this IoK8sApiAutoscalingV1CrossVersionObjectReference.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'api_version': str,
            'kind': str,
            'name': str
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'name': 'name'
        }

        self._api_version = api_version
        self._kind = kind
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAutoscalingV1CrossVersionObjectReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.autoscaling.v1.CrossVersionObjectReference of this IoK8sApiAutoscalingV1CrossVersionObjectReference.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV1CrossVersionObjectReference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        API version of the referent  # noqa: E501

        :return: The api_version of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        API version of the referent  # noqa: E501

        :param api_version: The api_version of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds\"  # noqa: E501

        :return: The kind of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds\"  # noqa: E501

        :param kind: The kind of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :type kind: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :return: The name of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApiAutoscalingV1CrossVersionObjectReference.

        Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :param name: The name of this IoK8sApiAutoscalingV1CrossVersionObjectReference.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
