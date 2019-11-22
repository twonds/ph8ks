# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, webhooks: List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]=None):  # noqa: E501
        """IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.  # noqa: E501
        :type api_version: str
        :param kind: The kind of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param webhooks: The webhooks of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.  # noqa: E501
        :type webhooks: List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]
        """
        self.swagger_types = {
            'api_version': str,
            'kind': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'webhooks': List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'metadata': 'metadata',
            'webhooks': 'webhooks'
        }

        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._webhooks = webhooks

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.admissionregistration.v1.ValidatingWebhookConfiguration of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.  # noqa: E501
        :rtype: IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.  # noqa: E501

        :return: The metadata of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.  # noqa: E501

        :param metadata: The metadata of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def webhooks(self) -> List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]:
        """Gets the webhooks of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Webhooks is a list of webhooks and the affected resources and operations.  # noqa: E501

        :return: The webhooks of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :rtype: List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks: List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]):
        """Sets the webhooks of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.

        Webhooks is a list of webhooks and the affected resources and operations.  # noqa: E501

        :param webhooks: The webhooks of this IoK8sApiAdmissionregistrationV1ValidatingWebhookConfiguration.
        :type webhooks: List[IoK8sApiAdmissionregistrationV1ValidatingWebhook]
        """

        self._webhooks = webhooks