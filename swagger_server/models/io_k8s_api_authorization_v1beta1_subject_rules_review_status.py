# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, evaluation_error: str=None, incomplete: bool=None, non_resource_rules: List[IoK8sApiAuthorizationV1beta1NonResourceRule]=None, resource_rules: List[IoK8sApiAuthorizationV1beta1ResourceRule]=None):  # noqa: E501
        """IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus - a model defined in Swagger

        :param evaluation_error: The evaluation_error of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.  # noqa: E501
        :type evaluation_error: str
        :param incomplete: The incomplete of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.  # noqa: E501
        :type incomplete: bool
        :param non_resource_rules: The non_resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.  # noqa: E501
        :type non_resource_rules: List[IoK8sApiAuthorizationV1beta1NonResourceRule]
        :param resource_rules: The resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.  # noqa: E501
        :type resource_rules: List[IoK8sApiAuthorizationV1beta1ResourceRule]
        """
        self.swagger_types = {
            'evaluation_error': str,
            'incomplete': bool,
            'non_resource_rules': List[IoK8sApiAuthorizationV1beta1NonResourceRule],
            'resource_rules': List[IoK8sApiAuthorizationV1beta1ResourceRule]
        }

        self.attribute_map = {
            'evaluation_error': 'evaluationError',
            'incomplete': 'incomplete',
            'non_resource_rules': 'nonResourceRules',
            'resource_rules': 'resourceRules'
        }

        self._evaluation_error = evaluation_error
        self._incomplete = incomplete
        self._non_resource_rules = non_resource_rules
        self._resource_rules = resource_rules

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authorization.v1beta1.SubjectRulesReviewStatus of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.  # noqa: E501
        :rtype: IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def evaluation_error(self) -> str:
        """Gets the evaluation_error of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.  # noqa: E501

        :return: The evaluation_error of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :rtype: str
        """
        return self._evaluation_error

    @evaluation_error.setter
    def evaluation_error(self, evaluation_error: str):
        """Sets the evaluation_error of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.  # noqa: E501

        :param evaluation_error: The evaluation_error of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :type evaluation_error: str
        """

        self._evaluation_error = evaluation_error

    @property
    def incomplete(self) -> bool:
        """Gets the incomplete of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.  # noqa: E501

        :return: The incomplete of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :rtype: bool
        """
        return self._incomplete

    @incomplete.setter
    def incomplete(self, incomplete: bool):
        """Sets the incomplete of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.  # noqa: E501

        :param incomplete: The incomplete of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :type incomplete: bool
        """
        if incomplete is None:
            raise ValueError("Invalid value for `incomplete`, must not be `None`")  # noqa: E501

        self._incomplete = incomplete

    @property
    def non_resource_rules(self) -> List[IoK8sApiAuthorizationV1beta1NonResourceRule]:
        """Gets the non_resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :return: The non_resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :rtype: List[IoK8sApiAuthorizationV1beta1NonResourceRule]
        """
        return self._non_resource_rules

    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules: List[IoK8sApiAuthorizationV1beta1NonResourceRule]):
        """Sets the non_resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :param non_resource_rules: The non_resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :type non_resource_rules: List[IoK8sApiAuthorizationV1beta1NonResourceRule]
        """
        if non_resource_rules is None:
            raise ValueError("Invalid value for `non_resource_rules`, must not be `None`")  # noqa: E501

        self._non_resource_rules = non_resource_rules

    @property
    def resource_rules(self) -> List[IoK8sApiAuthorizationV1beta1ResourceRule]:
        """Gets the resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :return: The resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :rtype: List[IoK8sApiAuthorizationV1beta1ResourceRule]
        """
        return self._resource_rules

    @resource_rules.setter
    def resource_rules(self, resource_rules: List[IoK8sApiAuthorizationV1beta1ResourceRule]):
        """Sets the resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.

        ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :param resource_rules: The resource_rules of this IoK8sApiAuthorizationV1beta1SubjectRulesReviewStatus.
        :type resource_rules: List[IoK8sApiAuthorizationV1beta1ResourceRule]
        """
        if resource_rules is None:
            raise ValueError("Invalid value for `resource_rules`, must not be `None`")  # noqa: E501

        self._resource_rules = resource_rules
