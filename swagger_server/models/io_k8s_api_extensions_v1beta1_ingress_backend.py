# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1IngressBackend(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, service_name: str=None, service_port: IoK8sApimachineryPkgUtilIntstrIntOrString=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1IngressBackend - a model defined in Swagger

        :param service_name: The service_name of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :type service_name: str
        :param service_port: The service_port of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :type service_port: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        self.swagger_types = {
            'service_name': str,
            'service_port': IoK8sApimachineryPkgUtilIntstrIntOrString
        }

        self.attribute_map = {
            'service_name': 'serviceName',
            'service_port': 'servicePort'
        }

        self._service_name = service_name
        self._service_port = service_port

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1IngressBackend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.IngressBackend of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1IngressBackend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_name(self) -> str:
        """Gets the service_name of this IoK8sApiExtensionsV1beta1IngressBackend.

        Specifies the name of the referenced service.  # noqa: E501

        :return: The service_name of this IoK8sApiExtensionsV1beta1IngressBackend.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str):
        """Sets the service_name of this IoK8sApiExtensionsV1beta1IngressBackend.

        Specifies the name of the referenced service.  # noqa: E501

        :param service_name: The service_name of this IoK8sApiExtensionsV1beta1IngressBackend.
        :type service_name: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def service_port(self) -> IoK8sApimachineryPkgUtilIntstrIntOrString:
        """Gets the service_port of this IoK8sApiExtensionsV1beta1IngressBackend.

        Specifies the port of the referenced service.  # noqa: E501

        :return: The service_port of this IoK8sApiExtensionsV1beta1IngressBackend.
        :rtype: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port: IoK8sApimachineryPkgUtilIntstrIntOrString):
        """Sets the service_port of this IoK8sApiExtensionsV1beta1IngressBackend.

        Specifies the port of the referenced service.  # noqa: E501

        :param service_port: The service_port of this IoK8sApiExtensionsV1beta1IngressBackend.
        :type service_port: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        if service_port is None:
            raise ValueError("Invalid value for `service_port`, must not be `None`")  # noqa: E501

        self._service_port = service_port
