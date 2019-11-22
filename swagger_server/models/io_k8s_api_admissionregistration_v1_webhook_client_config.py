# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAdmissionregistrationV1WebhookClientConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ca_bundle: ByteArray=None, service: IoK8sApiAdmissionregistrationV1ServiceReference=None, url: str=None):  # noqa: E501
        """IoK8sApiAdmissionregistrationV1WebhookClientConfig - a model defined in Swagger

        :param ca_bundle: The ca_bundle of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.  # noqa: E501
        :type ca_bundle: ByteArray
        :param service: The service of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.  # noqa: E501
        :type service: IoK8sApiAdmissionregistrationV1ServiceReference
        :param url: The url of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'ca_bundle': ByteArray,
            'service': IoK8sApiAdmissionregistrationV1ServiceReference,
            'url': str
        }

        self.attribute_map = {
            'ca_bundle': 'caBundle',
            'service': 'service',
            'url': 'url'
        }

        self._ca_bundle = ca_bundle
        self._service = service
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAdmissionregistrationV1WebhookClientConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.admissionregistration.v1.WebhookClientConfig of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.  # noqa: E501
        :rtype: IoK8sApiAdmissionregistrationV1WebhookClientConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ca_bundle(self) -> ByteArray:
        """Gets the ca_bundle of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :return: The ca_bundle of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :rtype: ByteArray
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle: ByteArray):
        """Sets the ca_bundle of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :param ca_bundle: The ca_bundle of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :type ca_bundle: ByteArray
        """
        if ca_bundle is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', ca_bundle):  # noqa: E501
            raise ValueError("Invalid value for `ca_bundle`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._ca_bundle = ca_bundle

    @property
    def service(self) -> IoK8sApiAdmissionregistrationV1ServiceReference:
        """Gets the service of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.  If the webhook is running within the cluster, then you should use `service`.  # noqa: E501

        :return: The service of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :rtype: IoK8sApiAdmissionregistrationV1ServiceReference
        """
        return self._service

    @service.setter
    def service(self, service: IoK8sApiAdmissionregistrationV1ServiceReference):
        """Sets the service of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.  If the webhook is running within the cluster, then you should use `service`.  # noqa: E501

        :param service: The service of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :type service: IoK8sApiAdmissionregistrationV1ServiceReference
        """

        self._service = service

    @property
    def url(self) -> str:
        """Gets the url of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.  # noqa: E501

        :return: The url of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.

        `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.  # noqa: E501

        :param url: The url of this IoK8sApiAdmissionregistrationV1WebhookClientConfig.
        :type url: str
        """

        self._url = url