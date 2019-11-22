# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1ScaleStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, replicas: int=None, selector: Dict[str, str]=None, target_selector: str=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1ScaleStatus - a model defined in Swagger

        :param replicas: The replicas of this IoK8sApiExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type replicas: int
        :param selector: The selector of this IoK8sApiExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type selector: Dict[str, str]
        :param target_selector: The target_selector of this IoK8sApiExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type target_selector: str
        """
        self.swagger_types = {
            'replicas': int,
            'selector': Dict[str, str],
            'target_selector': str
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'selector': 'selector',
            'target_selector': 'targetSelector'
        }

        self._replicas = replicas
        self._selector = selector
        self._target_selector = target_selector

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1ScaleStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.ScaleStatus of this IoK8sApiExtensionsV1beta1ScaleStatus.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1ScaleStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiExtensionsV1beta1ScaleStatus.

        actual number of observed instances of the scaled object.  # noqa: E501

        :return: The replicas of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiExtensionsV1beta1ScaleStatus.

        actual number of observed instances of the scaled object.  # noqa: E501

        :param replicas: The replicas of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :type replicas: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def selector(self) -> Dict[str, str]:
        """Gets the selector of this IoK8sApiExtensionsV1beta1ScaleStatus.

        label query over pods that should match the replicas count. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :return: The selector of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :rtype: Dict[str, str]
        """
        return self._selector

    @selector.setter
    def selector(self, selector: Dict[str, str]):
        """Sets the selector of this IoK8sApiExtensionsV1beta1ScaleStatus.

        label query over pods that should match the replicas count. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :param selector: The selector of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :type selector: Dict[str, str]
        """

        self._selector = selector

    @property
    def target_selector(self) -> str:
        """Gets the target_selector of this IoK8sApiExtensionsV1beta1ScaleStatus.

        label selector for pods that should match the replicas count. This is a serializated version of both map-based and more expressive set-based selectors. This is done to avoid introspection in the clients. The string will be in the same format as the query-param syntax. If the target type only supports map-based selectors, both this field and map-based selector field are populated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The target_selector of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :rtype: str
        """
        return self._target_selector

    @target_selector.setter
    def target_selector(self, target_selector: str):
        """Sets the target_selector of this IoK8sApiExtensionsV1beta1ScaleStatus.

        label selector for pods that should match the replicas count. This is a serializated version of both map-based and more expressive set-based selectors. This is done to avoid introspection in the clients. The string will be in the same format as the query-param syntax. If the target type only supports map-based selectors, both this field and map-based selector field are populated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param target_selector: The target_selector of this IoK8sApiExtensionsV1beta1ScaleStatus.
        :type target_selector: str
        """

        self._target_selector = target_selector
