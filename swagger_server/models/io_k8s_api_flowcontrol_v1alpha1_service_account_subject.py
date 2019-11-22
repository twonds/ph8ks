# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, namespace: str=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject - a model defined in Swagger

        :param name: The name of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.  # noqa: E501
        :type name: str
        :param namespace: The namespace of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.  # noqa: E501
        :type namespace: str
        """
        self.swagger_types = {
            'name': str,
            'namespace': str
        }

        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace'
        }

        self._name = name
        self._namespace = namespace

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.flowcontrol.v1alpha1.ServiceAccountSubject of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.

        `name` is the name of matching ServiceAccount objects, or \"*\" to match regardless of name. Required.  # noqa: E501

        :return: The name of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.

        `name` is the name of matching ServiceAccount objects, or \"*\" to match regardless of name. Required.  # noqa: E501

        :param name: The name of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self) -> str:
        """Gets the namespace of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.

        `namespace` is the namespace of matching ServiceAccount objects. Required.  # noqa: E501

        :return: The namespace of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.

        `namespace` is the namespace of matching ServiceAccount objects. Required.  # noqa: E501

        :param namespace: The namespace of this IoK8sApiFlowcontrolV1alpha1ServiceAccountSubject.
        :type namespace: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace