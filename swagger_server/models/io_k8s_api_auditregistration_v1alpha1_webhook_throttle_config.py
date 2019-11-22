# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, burst: int=None, qps: int=None):  # noqa: E501
        """IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig - a model defined in Swagger

        :param burst: The burst of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.  # noqa: E501
        :type burst: int
        :param qps: The qps of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.  # noqa: E501
        :type qps: int
        """
        self.swagger_types = {
            'burst': int,
            'qps': int
        }

        self.attribute_map = {
            'burst': 'burst',
            'qps': 'qps'
        }

        self._burst = burst
        self._qps = qps

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.auditregistration.v1alpha1.WebhookThrottleConfig of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.  # noqa: E501
        :rtype: IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def burst(self) -> int:
        """Gets the burst of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.

        ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS  # noqa: E501

        :return: The burst of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.
        :rtype: int
        """
        return self._burst

    @burst.setter
    def burst(self, burst: int):
        """Sets the burst of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.

        ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS  # noqa: E501

        :param burst: The burst of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.
        :type burst: int
        """

        self._burst = burst

    @property
    def qps(self) -> int:
        """Gets the qps of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.

        ThrottleQPS maximum number of batches per second default 10 QPS  # noqa: E501

        :return: The qps of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps: int):
        """Sets the qps of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.

        ThrottleQPS maximum number of batches per second default 10 QPS  # noqa: E501

        :param qps: The qps of this IoK8sApiAuditregistrationV1alpha1WebhookThrottleConfig.
        :type qps: int
        """

        self._qps = qps