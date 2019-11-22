# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuditregistrationV1alpha1AuditSinkSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, policy: IoK8sApiAuditregistrationV1alpha1Policy=None, webhook: IoK8sApiAuditregistrationV1alpha1Webhook=None):  # noqa: E501
        """IoK8sApiAuditregistrationV1alpha1AuditSinkSpec - a model defined in Swagger

        :param policy: The policy of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.  # noqa: E501
        :type policy: IoK8sApiAuditregistrationV1alpha1Policy
        :param webhook: The webhook of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.  # noqa: E501
        :type webhook: IoK8sApiAuditregistrationV1alpha1Webhook
        """
        self.swagger_types = {
            'policy': IoK8sApiAuditregistrationV1alpha1Policy,
            'webhook': IoK8sApiAuditregistrationV1alpha1Webhook
        }

        self.attribute_map = {
            'policy': 'policy',
            'webhook': 'webhook'
        }

        self._policy = policy
        self._webhook = webhook

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuditregistrationV1alpha1AuditSinkSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.auditregistration.v1alpha1.AuditSinkSpec of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.  # noqa: E501
        :rtype: IoK8sApiAuditregistrationV1alpha1AuditSinkSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def policy(self) -> IoK8sApiAuditregistrationV1alpha1Policy:
        """Gets the policy of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.

        Policy defines the policy for selecting which events should be sent to the webhook required  # noqa: E501

        :return: The policy of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.
        :rtype: IoK8sApiAuditregistrationV1alpha1Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy: IoK8sApiAuditregistrationV1alpha1Policy):
        """Sets the policy of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.

        Policy defines the policy for selecting which events should be sent to the webhook required  # noqa: E501

        :param policy: The policy of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.
        :type policy: IoK8sApiAuditregistrationV1alpha1Policy
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def webhook(self) -> IoK8sApiAuditregistrationV1alpha1Webhook:
        """Gets the webhook of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.

        Webhook to send events required  # noqa: E501

        :return: The webhook of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.
        :rtype: IoK8sApiAuditregistrationV1alpha1Webhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook: IoK8sApiAuditregistrationV1alpha1Webhook):
        """Sets the webhook of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.

        Webhook to send events required  # noqa: E501

        :param webhook: The webhook of this IoK8sApiAuditregistrationV1alpha1AuditSinkSpec.
        :type webhook: IoK8sApiAuditregistrationV1alpha1Webhook
        """
        if webhook is None:
            raise ValueError("Invalid value for `webhook`, must not be `None`")  # noqa: E501

        self._webhook = webhook