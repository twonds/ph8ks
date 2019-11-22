# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAppsV1StatefulSetSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pod_management_policy: str=None, replicas: int=None, revision_history_limit: int=None, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector=None, service_name: str=None, template: IoK8sApiCoreV1PodTemplateSpec=None, update_strategy: IoK8sApiAppsV1StatefulSetUpdateStrategy=None, volume_claim_templates: List[IoK8sApiCoreV1PersistentVolumeClaim]=None):  # noqa: E501
        """IoK8sApiAppsV1StatefulSetSpec - a model defined in Swagger

        :param pod_management_policy: The pod_management_policy of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type pod_management_policy: str
        :param replicas: The replicas of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type replicas: int
        :param revision_history_limit: The revision_history_limit of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type revision_history_limit: int
        :param selector: The selector of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        :param service_name: The service_name of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type service_name: str
        :param template: The template of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type template: IoK8sApiCoreV1PodTemplateSpec
        :param update_strategy: The update_strategy of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type update_strategy: IoK8sApiAppsV1StatefulSetUpdateStrategy
        :param volume_claim_templates: The volume_claim_templates of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :type volume_claim_templates: List[IoK8sApiCoreV1PersistentVolumeClaim]
        """
        self.swagger_types = {
            'pod_management_policy': str,
            'replicas': int,
            'revision_history_limit': int,
            'selector': IoK8sApimachineryPkgApisMetaV1LabelSelector,
            'service_name': str,
            'template': IoK8sApiCoreV1PodTemplateSpec,
            'update_strategy': IoK8sApiAppsV1StatefulSetUpdateStrategy,
            'volume_claim_templates': List[IoK8sApiCoreV1PersistentVolumeClaim]
        }

        self.attribute_map = {
            'pod_management_policy': 'podManagementPolicy',
            'replicas': 'replicas',
            'revision_history_limit': 'revisionHistoryLimit',
            'selector': 'selector',
            'service_name': 'serviceName',
            'template': 'template',
            'update_strategy': 'updateStrategy',
            'volume_claim_templates': 'volumeClaimTemplates'
        }

        self._pod_management_policy = pod_management_policy
        self._replicas = replicas
        self._revision_history_limit = revision_history_limit
        self._selector = selector
        self._service_name = service_name
        self._template = template
        self._update_strategy = update_strategy
        self._volume_claim_templates = volume_claim_templates

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAppsV1StatefulSetSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.apps.v1.StatefulSetSpec of this IoK8sApiAppsV1StatefulSetSpec.  # noqa: E501
        :rtype: IoK8sApiAppsV1StatefulSetSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pod_management_policy(self) -> str:
        """Gets the pod_management_policy of this IoK8sApiAppsV1StatefulSetSpec.

        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.  # noqa: E501

        :return: The pod_management_policy of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: str
        """
        return self._pod_management_policy

    @pod_management_policy.setter
    def pod_management_policy(self, pod_management_policy: str):
        """Sets the pod_management_policy of this IoK8sApiAppsV1StatefulSetSpec.

        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.  # noqa: E501

        :param pod_management_policy: The pod_management_policy of this IoK8sApiAppsV1StatefulSetSpec.
        :type pod_management_policy: str
        """

        self._pod_management_policy = pod_management_policy

    @property
    def replicas(self) -> int:
        """Gets the replicas of this IoK8sApiAppsV1StatefulSetSpec.

        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.  # noqa: E501

        :return: The replicas of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas: int):
        """Sets the replicas of this IoK8sApiAppsV1StatefulSetSpec.

        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAppsV1StatefulSetSpec.
        :type replicas: int
        """

        self._replicas = replicas

    @property
    def revision_history_limit(self) -> int:
        """Gets the revision_history_limit of this IoK8sApiAppsV1StatefulSetSpec.

        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.  # noqa: E501

        :return: The revision_history_limit of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit: int):
        """Sets the revision_history_limit of this IoK8sApiAppsV1StatefulSetSpec.

        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this IoK8sApiAppsV1StatefulSetSpec.
        :type revision_history_limit: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self) -> IoK8sApimachineryPkgApisMetaV1LabelSelector:
        """Gets the selector of this IoK8sApiAppsV1StatefulSetSpec.

        selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The selector of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector):
        """Sets the selector of this IoK8sApiAppsV1StatefulSetSpec.

        selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param selector: The selector of this IoK8sApiAppsV1StatefulSetSpec.
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def service_name(self) -> str:
        """Gets the service_name of this IoK8sApiAppsV1StatefulSetSpec.

        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.  # noqa: E501

        :return: The service_name of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str):
        """Sets the service_name of this IoK8sApiAppsV1StatefulSetSpec.

        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.  # noqa: E501

        :param service_name: The service_name of this IoK8sApiAppsV1StatefulSetSpec.
        :type service_name: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def template(self) -> IoK8sApiCoreV1PodTemplateSpec:
        """Gets the template of this IoK8sApiAppsV1StatefulSetSpec.

        template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.  # noqa: E501

        :return: The template of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: IoK8sApiCoreV1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template: IoK8sApiCoreV1PodTemplateSpec):
        """Sets the template of this IoK8sApiAppsV1StatefulSetSpec.

        template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.  # noqa: E501

        :param template: The template of this IoK8sApiAppsV1StatefulSetSpec.
        :type template: IoK8sApiCoreV1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def update_strategy(self) -> IoK8sApiAppsV1StatefulSetUpdateStrategy:
        """Gets the update_strategy of this IoK8sApiAppsV1StatefulSetSpec.

        updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.  # noqa: E501

        :return: The update_strategy of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: IoK8sApiAppsV1StatefulSetUpdateStrategy
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy: IoK8sApiAppsV1StatefulSetUpdateStrategy):
        """Sets the update_strategy of this IoK8sApiAppsV1StatefulSetSpec.

        updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.  # noqa: E501

        :param update_strategy: The update_strategy of this IoK8sApiAppsV1StatefulSetSpec.
        :type update_strategy: IoK8sApiAppsV1StatefulSetUpdateStrategy
        """

        self._update_strategy = update_strategy

    @property
    def volume_claim_templates(self) -> List[IoK8sApiCoreV1PersistentVolumeClaim]:
        """Gets the volume_claim_templates of this IoK8sApiAppsV1StatefulSetSpec.

        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.  # noqa: E501

        :return: The volume_claim_templates of this IoK8sApiAppsV1StatefulSetSpec.
        :rtype: List[IoK8sApiCoreV1PersistentVolumeClaim]
        """
        return self._volume_claim_templates

    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates: List[IoK8sApiCoreV1PersistentVolumeClaim]):
        """Sets the volume_claim_templates of this IoK8sApiAppsV1StatefulSetSpec.

        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.  # noqa: E501

        :param volume_claim_templates: The volume_claim_templates of this IoK8sApiAppsV1StatefulSetSpec.
        :type volume_claim_templates: List[IoK8sApiCoreV1PersistentVolumeClaim]
        """

        self._volume_claim_templates = volume_claim_templates
