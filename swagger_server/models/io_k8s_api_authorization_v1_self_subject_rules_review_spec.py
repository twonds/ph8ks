# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, namespace: str=None):  # noqa: E501
        """IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec - a model defined in Swagger

        :param namespace: The namespace of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.  # noqa: E501
        :type namespace: str
        """
        self.swagger_types = {
            'namespace': str
        }

        self.attribute_map = {
            'namespace': 'namespace'
        }

        self._namespace = namespace

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authorization.v1.SelfSubjectRulesReviewSpec of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.  # noqa: E501
        :rtype: IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def namespace(self) -> str:
        """Gets the namespace of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.

        Namespace to evaluate rules for. Required.  # noqa: E501

        :return: The namespace of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.

        Namespace to evaluate rules for. Required.  # noqa: E501

        :param namespace: The namespace of this IoK8sApiAuthorizationV1SelfSubjectRulesReviewSpec.
        :type namespace: str
        """

        self._namespace = namespace
