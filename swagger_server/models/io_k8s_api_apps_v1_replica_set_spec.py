# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1ReplicaSetSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, min_ready_seconds: int=None, replicas: int=None, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector=None, template: IoK8sApiCoreV1PodTemplateSpec=None):  # noqa: E501
        """IoK8sApiAppsV1ReplicaSetSpec - a model defined in Swagger

        :param min_ready_seconds: The min_ready_seconds of this IoK8sApiAppsV1ReplicaSetSpec.  # noqa: E501
        :type min_ready_seconds: int
        :param replicas: The replicas of this IoK8sApiAppsV1ReplicaSetSpec.  # noqa: E501
        :type replicas: int
        :param selector: The selector of this IoK8sApiAppsV1ReplicaSetSpec.  # noqa: E501
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        :param template: The template of this IoK8sApiAppsV1ReplicaSetSpec.  # noqa: E501
        :type template: IoK8sApiCoreV1PodTemplateSpec
        """
        self.swagger_types = {
            'min_ready_seconds': int,
            'replicas': int,
            'selector': IoK8sApimachineryPkgApisMetaV1LabelSelector,
            'template': IoK8sApiCoreV1PodTemplateSpec
        }

        self.attribute_map = {
            'min_ready_seconds': 'minReadySeconds',
            'replicas': 'replicas',
            'selector': 'selector',
            'template': 'template'
        }

        self._min_ready_seconds = min_ready_seconds
        self._replicas = replicas
        self._selector = selector
        self._template = template

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1ReplicaSetSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1.ReplicaSetSpec of this IoK8sApiAppsV1ReplicaSetSpec.  # noqa: E501
        :rtype: IoK8sApiAppsV1ReplicaSetSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_ready_seconds(self) -> int:
        """Gets the min_ready_seconds of this IoK8sApiAppsV1ReplicaSetSpec.

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :return: The min_ready_seconds of this IoK8sApiAppsV1ReplicaSetSpec.
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds: int):
        """Sets the min_ready_seconds of this IoK8sApiAppsV1ReplicaSetSpec.

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this IoK8sApiAppsV1ReplicaSetSpec.
        :type min_ready_seconds: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiAppsV1ReplicaSetSpec.

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :return: The replicas of this IoK8sApiAppsV1ReplicaSetSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiAppsV1ReplicaSetSpec.

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAppsV1ReplicaSetSpec.
        :type replicas: int
        """

        self._replicas = replicas

    @property
    def selector(self) -> IoK8sApimachineryPkgApisMetaV1LabelSelector:
        """Gets the selector of this IoK8sApiAppsV1ReplicaSetSpec.

        Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The selector of this IoK8sApiAppsV1ReplicaSetSpec.
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector):
        """Sets the selector of this IoK8sApiAppsV1ReplicaSetSpec.

        Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param selector: The selector of this IoK8sApiAppsV1ReplicaSetSpec.
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def template(self) -> IoK8sApiCoreV1PodTemplateSpec:
        """Gets the template of this IoK8sApiAppsV1ReplicaSetSpec.

        Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :return: The template of this IoK8sApiAppsV1ReplicaSetSpec.
        :rtype: IoK8sApiCoreV1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template: IoK8sApiCoreV1PodTemplateSpec):
        """Sets the template of this IoK8sApiAppsV1ReplicaSetSpec.

        Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :param template: The template of this IoK8sApiAppsV1ReplicaSetSpec.
        :type template: IoK8sApiCoreV1PodTemplateSpec
        """

        self._template = template
