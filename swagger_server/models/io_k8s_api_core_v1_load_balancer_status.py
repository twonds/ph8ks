# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1LoadBalancerStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ingress: List[IoK8sApiCoreV1LoadBalancerIngress]=None):  # noqa: E501
        """IoK8sApiCoreV1LoadBalancerStatus - a model defined in Swagger

        :param ingress: The ingress of this IoK8sApiCoreV1LoadBalancerStatus.  # noqa: E501
        :type ingress: List[IoK8sApiCoreV1LoadBalancerIngress]
        """
        self.swagger_types = {
            'ingress': List[IoK8sApiCoreV1LoadBalancerIngress]
        }

        self.attribute_map = {
            'ingress': 'ingress'
        }

        self._ingress = ingress

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1LoadBalancerStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.LoadBalancerStatus of this IoK8sApiCoreV1LoadBalancerStatus.  # noqa: E501
        :rtype: IoK8sApiCoreV1LoadBalancerStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ingress(self) -> List[IoK8sApiCoreV1LoadBalancerIngress]:
        """Gets the ingress of this IoK8sApiCoreV1LoadBalancerStatus.

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.  # noqa: E501

        :return: The ingress of this IoK8sApiCoreV1LoadBalancerStatus.
        :rtype: List[IoK8sApiCoreV1LoadBalancerIngress]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress: List[IoK8sApiCoreV1LoadBalancerIngress]):
        """Sets the ingress of this IoK8sApiCoreV1LoadBalancerStatus.

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.  # noqa: E501

        :param ingress: The ingress of this IoK8sApiCoreV1LoadBalancerStatus.
        :type ingress: List[IoK8sApiCoreV1LoadBalancerIngress]
        """

        self._ingress = ingress
