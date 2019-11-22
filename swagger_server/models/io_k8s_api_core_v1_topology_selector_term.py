# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1TopologySelectorTerm(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, match_label_expressions: List[IoK8sApiCoreV1TopologySelectorLabelRequirement]=None):  # noqa: E501
        """IoK8sApiCoreV1TopologySelectorTerm - a model defined in Swagger

        :param match_label_expressions: The match_label_expressions of this IoK8sApiCoreV1TopologySelectorTerm.  # noqa: E501
        :type match_label_expressions: List[IoK8sApiCoreV1TopologySelectorLabelRequirement]
        """
        self.swagger_types = {
            'match_label_expressions': List[IoK8sApiCoreV1TopologySelectorLabelRequirement]
        }

        self.attribute_map = {
            'match_label_expressions': 'matchLabelExpressions'
        }

        self._match_label_expressions = match_label_expressions

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1TopologySelectorTerm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.TopologySelectorTerm of this IoK8sApiCoreV1TopologySelectorTerm.  # noqa: E501
        :rtype: IoK8sApiCoreV1TopologySelectorTerm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def match_label_expressions(self) -> List[IoK8sApiCoreV1TopologySelectorLabelRequirement]:
        """Gets the match_label_expressions of this IoK8sApiCoreV1TopologySelectorTerm.

        A list of topology selector requirements by labels.  # noqa: E501

        :return: The match_label_expressions of this IoK8sApiCoreV1TopologySelectorTerm.
        :rtype: List[IoK8sApiCoreV1TopologySelectorLabelRequirement]
        """
        return self._match_label_expressions

    @match_label_expressions.setter
    def match_label_expressions(self, match_label_expressions: List[IoK8sApiCoreV1TopologySelectorLabelRequirement]):
        """Sets the match_label_expressions of this IoK8sApiCoreV1TopologySelectorTerm.

        A list of topology selector requirements by labels.  # noqa: E501

        :param match_label_expressions: The match_label_expressions of this IoK8sApiCoreV1TopologySelectorTerm.
        :type match_label_expressions: List[IoK8sApiCoreV1TopologySelectorLabelRequirement]
        """

        self._match_label_expressions = match_label_expressions