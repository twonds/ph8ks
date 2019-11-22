# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiNetworkingV1beta1HTTPIngressPath(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, backend: IoK8sApiNetworkingV1beta1IngressBackend=None, path: str=None):  # noqa: E501
        """IoK8sApiNetworkingV1beta1HTTPIngressPath - a model defined in Swagger

        :param backend: The backend of this IoK8sApiNetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :type backend: IoK8sApiNetworkingV1beta1IngressBackend
        :param path: The path of this IoK8sApiNetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :type path: str
        """
        self.swagger_types = {
            'backend': IoK8sApiNetworkingV1beta1IngressBackend,
            'path': str
        }

        self.attribute_map = {
            'backend': 'backend',
            'path': 'path'
        }

        self._backend = backend
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiNetworkingV1beta1HTTPIngressPath':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.networking.v1beta1.HTTPIngressPath of this IoK8sApiNetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :rtype: IoK8sApiNetworkingV1beta1HTTPIngressPath
        """
        return util.deserialize_model(dikt, cls)

    @property
    def backend(self) -> IoK8sApiNetworkingV1beta1IngressBackend:
        """Gets the backend of this IoK8sApiNetworkingV1beta1HTTPIngressPath.

        Backend defines the referenced service endpoint to which the traffic will be forwarded to.  # noqa: E501

        :return: The backend of this IoK8sApiNetworkingV1beta1HTTPIngressPath.
        :rtype: IoK8sApiNetworkingV1beta1IngressBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend: IoK8sApiNetworkingV1beta1IngressBackend):
        """Sets the backend of this IoK8sApiNetworkingV1beta1HTTPIngressPath.

        Backend defines the referenced service endpoint to which the traffic will be forwarded to.  # noqa: E501

        :param backend: The backend of this IoK8sApiNetworkingV1beta1HTTPIngressPath.
        :type backend: IoK8sApiNetworkingV1beta1IngressBackend
        """
        if backend is None:
            raise ValueError("Invalid value for `backend`, must not be `None`")  # noqa: E501

        self._backend = backend

    @property
    def path(self) -> str:
        """Gets the path of this IoK8sApiNetworkingV1beta1HTTPIngressPath.

        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.  # noqa: E501

        :return: The path of this IoK8sApiNetworkingV1beta1HTTPIngressPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this IoK8sApiNetworkingV1beta1HTTPIngressPath.

        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.  # noqa: E501

        :param path: The path of this IoK8sApiNetworkingV1beta1HTTPIngressPath.
        :type path: str
        """

        self._path = path