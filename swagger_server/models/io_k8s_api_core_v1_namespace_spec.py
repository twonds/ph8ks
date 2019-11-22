# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1NamespaceSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, finalizers: List[str]=None):  # noqa: E501
        """IoK8sApiCoreV1NamespaceSpec - a model defined in Swagger

        :param finalizers: The finalizers of this IoK8sApiCoreV1NamespaceSpec.  # noqa: E501
        :type finalizers: List[str]
        """
        self.swagger_types = {
            'finalizers': List[str]
        }

        self.attribute_map = {
            'finalizers': 'finalizers'
        }

        self._finalizers = finalizers

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1NamespaceSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.NamespaceSpec of this IoK8sApiCoreV1NamespaceSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1NamespaceSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def finalizers(self) -> List[str]:
        """Gets the finalizers of this IoK8sApiCoreV1NamespaceSpec.

        Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/  # noqa: E501

        :return: The finalizers of this IoK8sApiCoreV1NamespaceSpec.
        :rtype: List[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers: List[str]):
        """Sets the finalizers of this IoK8sApiCoreV1NamespaceSpec.

        Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/  # noqa: E501

        :param finalizers: The finalizers of this IoK8sApiCoreV1NamespaceSpec.
        :type finalizers: List[str]
        """

        self._finalizers = finalizers
