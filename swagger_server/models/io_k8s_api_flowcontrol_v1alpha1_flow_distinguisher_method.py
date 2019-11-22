# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod - a model defined in Swagger

        :param type: The type of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'type': str
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.flowcontrol.v1alpha1.FlowDistinguisherMethod of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.

        `type` is the type of flow distinguisher method The supported types are \"ByUser\" and \"ByNamespace\". Required.  # noqa: E501

        :return: The type of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.

        `type` is the type of flow distinguisher method The supported types are \"ByUser\" and \"ByNamespace\". Required.  # noqa: E501

        :param type: The type of this IoK8sApiFlowcontrolV1alpha1FlowDistinguisherMethod.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
