# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1IngressTLS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hosts: List[str]=None, secret_name: str=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1IngressTLS - a model defined in Swagger

        :param hosts: The hosts of this IoK8sApiExtensionsV1beta1IngressTLS.  # noqa: E501
        :type hosts: List[str]
        :param secret_name: The secret_name of this IoK8sApiExtensionsV1beta1IngressTLS.  # noqa: E501
        :type secret_name: str
        """
        self.swagger_types = {
            'hosts': List[str],
            'secret_name': str
        }

        self.attribute_map = {
            'hosts': 'hosts',
            'secret_name': 'secretName'
        }

        self._hosts = hosts
        self._secret_name = secret_name

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1IngressTLS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.IngressTLS of this IoK8sApiExtensionsV1beta1IngressTLS.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1IngressTLS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hosts(self) -> List[str]:
        """Gets the hosts of this IoK8sApiExtensionsV1beta1IngressTLS.

        Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.  # noqa: E501

        :return: The hosts of this IoK8sApiExtensionsV1beta1IngressTLS.
        :rtype: List[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts: List[str]):
        """Sets the hosts of this IoK8sApiExtensionsV1beta1IngressTLS.

        Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.  # noqa: E501

        :param hosts: The hosts of this IoK8sApiExtensionsV1beta1IngressTLS.
        :type hosts: List[str]
        """

        self._hosts = hosts

    @property
    def secret_name(self) -> str:
        """Gets the secret_name of this IoK8sApiExtensionsV1beta1IngressTLS.

        SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the \"Host\" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.  # noqa: E501

        :return: The secret_name of this IoK8sApiExtensionsV1beta1IngressTLS.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name: str):
        """Sets the secret_name of this IoK8sApiExtensionsV1beta1IngressTLS.

        SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the \"Host\" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.  # noqa: E501

        :param secret_name: The secret_name of this IoK8sApiExtensionsV1beta1IngressTLS.
        :type secret_name: str
        """

        self._secret_name = secret_name
